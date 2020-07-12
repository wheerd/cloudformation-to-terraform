import re
import functools
import importlib
import pkgutil

camel_case_pattern = re.compile(r"(?<=[^A-Z])(?=[A-Z])|(?<!^)(?=[A-Z][a-z])")


def camel_case_to_snake_case(string):
    return camel_case_pattern.sub("_", string).lower()


cnf_abbreviation_fixes = {
    "a_w_s": "aws",
    "e_c2": "ec2",
    "s_s_m": "ssm",
    "r_d_s": "rds",
    "e_c_s": "e_c_s",
    "io_t": "iot",
    "wa_fv2": "waf_v2",
    "elastic_load_balancing": "elb",
}


def snake_case_with_abbreviation_fix(name):
    name = camel_case_to_snake_case(name)
    return functools.reduce(lambda n, p: n.replace(*p), cnf_abbreviation_fixes.items(), name)


def import_submodules(package, recursive=True):
    """ Import all submodules of a module, recursively, including subpackages

    :param package: package (name or actual module)
    :type package: str | module
    :rtype: dict[str, types.ModuleType]
    """
    if isinstance(package, str):
        package = importlib.import_module(package)
    results = {}
    for loader, name, is_pkg in pkgutil.walk_packages(package.__path__):
        full_name = package.__name__ + "." + name
        results[full_name] = importlib.import_module(full_name)
        if recursive and is_pkg:
            results.update(import_submodules(full_name))
    return results


def topological_sort(source):
    """perform topo sort on elements.

    :arg source: list of ``(name, [list of dependancies])`` pairs
    :returns: list of names, with dependancies listed first
    """
    pending = [(name, set(deps) - set([name])) for name, deps in source]
    emitted = []
    while pending:
        next_pending = []
        next_emitted = []
        for entry in pending:
            name, deps = entry
            deps.difference_update(emitted)
            if deps:
                next_pending.append(entry)
            else:
                yield name
                emitted.append(name)
                next_emitted.append(name)
        if not next_emitted:
            for name, _ in next_pending:
                yield name
            return
        pending = next_pending
        emitted = next_emitted
