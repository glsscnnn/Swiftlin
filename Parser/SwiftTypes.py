# import requirement
import os
import sys
import re

""" Kotlin / Swift Types """

class BaseType(object):
    #  Heavily based on Cython's implmentation
    #  Base class for all Swiftlin types including pseudo-types.
    # List of attribute names of any subtypes

    subtypes = []
    _empty_declaration = None
    _specialization_name = None
    default_format_spec = None

    def can_coerce_to_swiftobject(self, env):
        return False

    def can_coerce_from_swiftobject(self, env):
        return False

    def can_coerce_to_swiftstring(self, env, format_spec=None):
        return False

    def convert_to_swiftstring(self, cvalue, code, format_spec=None):
        raise NotImplementedError("Swift types that support string formatting must override this method")

    def cast_code(self, expr_code):
        return "((%s)%s)" % (self.empty_declaration_code(), expr_code)

    def empty_declaration_code(self):
        if self._empty_declaration is None:
            self._empty_declaration = self.declaration_code('')
        return self._empty_declaration

    def specialization_name(self):
        if self._specialization_name is None:
            # This is not entirely robust.
            common_subs = (self.empty_declaration_code()
                           .replace("unsigned ", "unsigned_")
                           .replace("long long", "long_long")
                           .replace(" ", "__"))
            self._specialization_name = re.sub(
                '[^a-zA-Z0-9_]', lambda x: '_%x_' % ord(x.group(0)), common_subs)
        return self._specialization_name

    def base_declaration_code(self, base_code, entity_code):
        if entity_code:
            return "%s %s" % (base_code, entity_code)
        else:
            return base_code

    def get_fused_types(self, result=None, seen=None, subtypes=None):
        subtypes = subtypes or self.subtypes
        if not subtypes:
            return None

        if result is None:
            result = []
            seen = set()

        for attr in subtypes:
            list_or_subtype = getattr(self, attr)
            if list_or_subtype:
                if isinstance(list_or_subtype, BaseType):
                    list_or_subtype.get_fused_types(result, seen)
                else:
                    for subtype in list_or_subtype:
                        subtype.get_fused_types(result, seen)

        return result

    def specialize_fused(self, env):
        if env.fused_to_specific:
            return self.specialize(env.fused_to_specific)

        return self

    @property
    def is_fused(self):
        """
        Whether this type or any of its subtypes is a fused type
        """
        # Add this indirection for the is_fused property to allow overriding
        # get_fused_types in subclasses.
        return self.get_fused_types()

    def deduce_template_params(self, actual):
        """
        Deduce any template params in this (argument) type given the actual
        argument type.
        """
        return {}


    def swift_type_name(self):
        """
        Return the name of the Swift type that can coerce to this type.
        """

    def typeof_name(self):
        """
        Return the string with which fused swift functions can be indexed.
        """
        if self.is_builtin_type or self.swift_type_name() == 'object':
            index_name = self.swift_type_name()
        else:
            index_name = str(self)

        return index_name

class SwiftlinTypes(BaseType):
    """
    All Swiftlin Types:

    is_kotlin_object        boolean     is a kotlin object
    is_kotlin_function      boolean     is a kotlin function
    is_kotlin_list          boolean     is a kotlin list
    is_kotlin_map           boolean     is a kotlin map
    is_kotlin_set           boolean     is a kotlin set

    """
    pass