import re


def create_cluster_helper(cpu, mem, nodes, geoloc, name):
    pass


def create_cluster(tokens):
    format = 'format:\n\tcreate cluster <cpu> <mem>g <#-of-nodes> <geolocation> <optional-cluster-name>'
    if len(tokens) not in [4,5]:
        return format
    if len(tokens) == 4:
        tokens.append('cluster-1')
    
    cpu, mem, nodes, geo, name = tokens
    if not cpu.isnumeric():
        return format
    cpu = int(cpu)
    if cpu < 1 or cpu > 8:
        return 'cpu must between 1-4'
    
    if len(mem)<2 or mem[-1] != 'g' or not mem[:-1].isnumeric():
        return format
    mem = int(mem[:-1])
    if mem < 1 or mem > 4:
        return 'mem must between 1g-4g'
    
    if not nodes.isnumeric():
        return format
    nodes = int(nodes)
    if nodes < 1 or nodes > 4:
        return 'nodes must between 1-4'
    
    total_mem = mem*nodes
    total_cpu = cpu*nodes
    if total_cpu > 8:
        return f'Not enough money!\n{total_cpu} is just too many cpus. no more than 8 total cpus are allowed'
    if total_mem > 12:
        return f'Not enough money!\n{total_mem}g is just too much mem. no more than 12g total mem is allowed'

    geodict = {
        'ny': 'ny',
        'sf':'sf', 
        'london':'london', 
        'frankfurt':'frankfurt',
        'singapore':'singapore', 
        'lon':'london', 
        'fran':'frankfurt', 
        'sing':'singapore',
    }
    if geo not in list(geodict.keys()):
        return f'geo location must be one of:\n\t{", ".join(sorted(geodict.keys()))}'

    if len(name) < 3 or len(name) > 25:
        return 'cluster name must be 3-25 characters long'
    if not re.match(r'^[\w-]+$', name):
        return "invalid cluster name. Only alphanumeric, '-', and '_' characters are allowed"
    
    return f'creating new k8s cluster {name} ...'

def deploy(tokens):
    return 'deploying tranx...'

def destroy(tokens):
    return 'cluster destroyed'
