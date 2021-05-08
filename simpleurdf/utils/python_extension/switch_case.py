from typing import Callable, Dict, Type, Any, Optional, cast, TypeVar

DEFAULT = "default"
T = TypeVar('T')


def switch_case(unknown_type_object: object,
                all_cases: Dict[Optional[Type], Callable[[Any], T]]) -> T:
    for current_type in list(all_cases.keys()):
        if current_type is not None:
            if isinstance(unknown_type_object, current_type):
                return all_cases[current_type](unknown_type_object)
    return all_cases[None](unknown_type_object)


def case(unknown_type_object: object,
         check_type: Type,
         method_to_exe: Callable):
    if unknown_type_object.__class__ == check_type:
        return cast(check_type, unknown_type_object)
    return unknown_type_object
