import importlib
from actions.core.registry import REGISTRY

def execute(cmd):
    try:
        if isinstance(cmd, list):
            results = []
            for c in cmd:
                r = execute(c)
                results.append(r)
            return ", ".join([str(r) for r in results if r])
        path = cmd.get("path")
        args = cmd.get("args", {})
        func_path = REGISTRY.get(path)
        if not func_path:
            print(f"[Executor]: No function found for {path}")
            return None
        module_path, func_name = func_path.rsplit(".", 1)
        module = importlib.import_module(module_path)
        func = getattr(module, func_name)
        print(f"[Executor]: Running {func_path}")
        return func(**args)
    except Exception as e:
        print(f"[Executor Error]: {e}")
        return None
