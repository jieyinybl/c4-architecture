import os
import graphviz
import pathlib

from c4.architectures.dwh import dwh


def _content(element):
    return f'{element.name}\n\n{element.description}'


def c4_graph(context):
    attr = {'node_attr': {'shape': 'record',
                          'fontsize': '6'},
            'edge_attr': {'fontsize': '6',
                          'labelfontsize': '6'}}
    graph = graphviz.Digraph(**attr)
    graph.attr(compound='true', dpi='400')
    for person in context.persons:
        graph.node(name=_content(person))
        for usage in person.usages:
            graph.edge(_content(person), _content(usage.target), label=usage.description)
    for system in context.systems:
        graph.node(name=_content(system))
        with graph.subgraph(name=f'cluster_{system.name}') as c:
            c.attr(style='filled', color='lightgrey', label=system.name)
            c.node_attr['style'] = 'filled'
            for container in system.containers:
                c.edge(_content(system), _content(container))
                # for usage in container.usages:
                #    c.edge(_content(container), _content(usage.target))
                with graph.subgraph(name=f'cluster_{container.name}') as c2:
                    c2.attr(color='blue')
                    c2.node_attr['style'] = 'filled'
                    for component in container.components:
                        c2.node(_content(component))
                        graph.edge(_content(container), _content(component))
                    c2.attr(label=container.name)
            for usage in system.usages:
                graph.edge(_content(system), _content(usage.target), label=usage.description)

    graph.render(format='png', filename='architecture_graph', directory=pathlib.Path('c4/images/'))


c4_graph(dwh)
