import graphviz
import pathlib

default_attr = {'fontsize': '6'}


def _content_node(element):
    return f'{element.name}\n[{element.type}]\n\n{element.description}'


def _content_label(element):
    return f'{element.name} [{element.type}]'


def _content_relationship(relationship):
    if relationship.method:
        return f'{relationship.description}\n[{relationship.method}]'
    else:
        return f'{relationship.description}'


def c4_graph(context, format='png', filename='architecture_graph', directory=pathlib.Path('architectures/')):
    attr = {'graph_attr': {'fontsize': default_attr['fontsize'], },
            'node_attr': {'shape': 'box',
                          'fontsize': default_attr['fontsize'],
                          'fontcolor': 'white',
                          'style': 'filled'},
            'edge_attr': {'fontsize': default_attr['fontsize'],
                          'labelfontsize': '6'}}
    graph = graphviz.Digraph(**attr)
    graph.attr(compound='true', dpi='400')
    for person in context.persons:
        graph.node(name=_content_node(person), fillcolor='#08427B')
        for relationship in person.relationships:
            graph.edge(_content_node(person), _content_node(relationship.target), label=_content_relationship(relationship))
    for system in context.systems:
        color_system = '#1168BD' if system.internal else '#999999'
        graph.node(name=_content_node(system), fillcolor=color_system)
        for relationship in system.relationships:
            graph.edge(_content_node(system), _content_node(relationship.target), label=_content_relationship(relationship))
        with graph.subgraph(name=f'cluster_{system.name}') as c_system:
            c_system.attr(style='dotted', label=_content_label(system))
            if len(system.containers) > 0:
                ## draw the edge only once to keep the chart clean
                graph.edge(_content_node(system), _content_node(system.containers[0]), lhead=f'cluster_{system.name}')
            for container in system.containers:
                c_system.node(name=_content_node(container), style='filled', fillcolor='#438DD5')
                for relationship in container.relationships:
                    graph.edge(_content_node(container), _content_node(relationship.target), label=_content_relationship(relationship))
                cluster_container = f'cluster_{container.name}'
                with graph.subgraph(name=cluster_container) as c_container:
                    c_container.attr(style='dotted', label=_content_label(container))
                    if len(container.components) > 0:
                        graph.edge(_content_node(container), _content_node(container.components[0]),
                                   lhead=cluster_container)
                    for component in container.components:
                        c_container.node(_content_node(component), style='filled', fillcolor='#85BBF0')
                        for relationship in component.relationships:
                            graph.edge(_content_node(_content_node(component)), _content_node(relationship.target),
                                       label=_content_relationship(relationship))

    graph.render(format=format, filename=filename, directory=directory)
