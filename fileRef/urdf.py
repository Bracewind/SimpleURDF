# ./urdf.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:d186d36d3e3ae3fe33317cf477b3e757972ff8f2
# Generated 2021-04-20 19:24:10.107193 by PyXB version 1.2.6 using Python 3.8.5.final.0
# Namespace http://www.ros.org

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six
# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:fb5f01f2-a20d-11eb-addf-0242c5955170')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.6'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://www.ros.org', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Complex type {http://www.ros.org}pose with content type EMPTY
class pose (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.ros.org}pose with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'pose')
    _XSDLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 17, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute xyz uses Python identifier xyz
    __xyz = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'xyz'), 'xyz', '__httpwww_ros_org_pose_xyz', pyxb.binding.datatypes.string, unicode_default='0 0 0')
    __xyz._DeclarationLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 18, 4)
    __xyz._UseLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 18, 4)
    
    xyz = property(__xyz.value, __xyz.set, None, None)

    
    # Attribute rpy uses Python identifier rpy
    __rpy = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'rpy'), 'rpy', '__httpwww_ros_org_pose_rpy', pyxb.binding.datatypes.string, unicode_default='0 0 0')
    __rpy._DeclarationLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 19, 4)
    __rpy._UseLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 19, 4)
    
    rpy = property(__rpy.value, __rpy.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __xyz.name() : __xyz,
        __rpy.name() : __rpy
    })
_module_typeBindings.pose = pose
Namespace.addCategoryObject('typeBinding', 'pose', pose)


# Complex type {http://www.ros.org}color with content type EMPTY
class color (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.ros.org}color with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'color')
    _XSDLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 23, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute rgba uses Python identifier rgba
    __rgba = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'rgba'), 'rgba', '__httpwww_ros_org_color_rgba', pyxb.binding.datatypes.string, unicode_default='0 0 0 0')
    __rgba._DeclarationLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 24, 4)
    __rgba._UseLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 24, 4)
    
    rgba = property(__rgba.value, __rgba.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __rgba.name() : __rgba
    })
_module_typeBindings.color = color
Namespace.addCategoryObject('typeBinding', 'color', color)


# Complex type {http://www.ros.org}verbose with content type EMPTY
class verbose (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.ros.org}verbose with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'verbose')
    _XSDLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 28, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute value uses Python identifier value_
    __value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'value'), 'value_', '__httpwww_ros_org_verbose_value', pyxb.binding.datatypes.string)
    __value._DeclarationLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 29, 4)
    __value._UseLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 29, 4)
    
    value_ = property(__value.value, __value.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __value.name() : __value
    })
_module_typeBindings.verbose = verbose
Namespace.addCategoryObject('typeBinding', 'verbose', verbose)


# Complex type {http://www.ros.org}name with content type EMPTY
class name (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.ros.org}name with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'name')
    _XSDLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 33, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpwww_ros_org_name_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 34, 4)
    __name._UseLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 34, 4)
    
    name = property(__name.value, __name.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __name.name() : __name
    })
_module_typeBindings.name = name
Namespace.addCategoryObject('typeBinding', 'name', name)


# Complex type {http://www.ros.org}mass with content type EMPTY
class mass (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.ros.org}mass with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'mass')
    _XSDLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 39, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute value uses Python identifier value_
    __value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'value'), 'value_', '__httpwww_ros_org_mass_value', pyxb.binding.datatypes.double, unicode_default='0')
    __value._DeclarationLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 41, 4)
    __value._UseLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 41, 4)
    
    value_ = property(__value.value, __value.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __value.name() : __value
    })
_module_typeBindings.mass = mass
Namespace.addCategoryObject('typeBinding', 'mass', mass)


# Complex type {http://www.ros.org}inertia with content type EMPTY
class inertia (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.ros.org}inertia with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'inertia')
    _XSDLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 45, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute ixx uses Python identifier ixx
    __ixx = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ixx'), 'ixx', '__httpwww_ros_org_inertia_ixx', pyxb.binding.datatypes.double, unicode_default='0')
    __ixx._DeclarationLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 47, 4)
    __ixx._UseLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 47, 4)
    
    ixx = property(__ixx.value, __ixx.set, None, None)

    
    # Attribute ixy uses Python identifier ixy
    __ixy = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ixy'), 'ixy', '__httpwww_ros_org_inertia_ixy', pyxb.binding.datatypes.double, unicode_default='0')
    __ixy._DeclarationLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 48, 4)
    __ixy._UseLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 48, 4)
    
    ixy = property(__ixy.value, __ixy.set, None, None)

    
    # Attribute ixz uses Python identifier ixz
    __ixz = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ixz'), 'ixz', '__httpwww_ros_org_inertia_ixz', pyxb.binding.datatypes.double, unicode_default='0')
    __ixz._DeclarationLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 49, 4)
    __ixz._UseLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 49, 4)
    
    ixz = property(__ixz.value, __ixz.set, None, None)

    
    # Attribute iyy uses Python identifier iyy
    __iyy = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'iyy'), 'iyy', '__httpwww_ros_org_inertia_iyy', pyxb.binding.datatypes.double, unicode_default='0')
    __iyy._DeclarationLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 50, 4)
    __iyy._UseLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 50, 4)
    
    iyy = property(__iyy.value, __iyy.set, None, None)

    
    # Attribute iyz uses Python identifier iyz
    __iyz = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'iyz'), 'iyz', '__httpwww_ros_org_inertia_iyz', pyxb.binding.datatypes.double, unicode_default='0')
    __iyz._DeclarationLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 51, 4)
    __iyz._UseLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 51, 4)
    
    iyz = property(__iyz.value, __iyz.set, None, None)

    
    # Attribute izz uses Python identifier izz
    __izz = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'izz'), 'izz', '__httpwww_ros_org_inertia_izz', pyxb.binding.datatypes.double, unicode_default='0')
    __izz._DeclarationLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 52, 4)
    __izz._UseLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 52, 4)
    
    izz = property(__izz.value, __izz.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __ixx.name() : __ixx,
        __ixy.name() : __ixy,
        __ixz.name() : __ixz,
        __iyy.name() : __iyy,
        __iyz.name() : __iyz,
        __izz.name() : __izz
    })
_module_typeBindings.inertia = inertia
Namespace.addCategoryObject('typeBinding', 'inertia', inertia)


# Complex type {http://www.ros.org}inertial with content type ELEMENT_ONLY
class inertial (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.ros.org}inertial with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'inertial')
    _XSDLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 56, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.ros.org}origin uses Python identifier origin
    __origin = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'origin'), 'origin', '__httpwww_ros_org_inertial_httpwww_ros_orgorigin', False, pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 58, 6), )

    
    origin = property(__origin.value, __origin.set, None, None)

    
    # Element {http://www.ros.org}mass uses Python identifier mass
    __mass = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'mass'), 'mass', '__httpwww_ros_org_inertial_httpwww_ros_orgmass', False, pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 60, 6), )

    
    mass = property(__mass.value, __mass.set, None, None)

    
    # Element {http://www.ros.org}inertia uses Python identifier inertia
    __inertia = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'inertia'), 'inertia', '__httpwww_ros_org_inertial_httpwww_ros_orginertia', False, pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 62, 6), )

    
    inertia = property(__inertia.value, __inertia.set, None, None)

    _ElementMap.update({
        __origin.name() : __origin,
        __mass.name() : __mass,
        __inertia.name() : __inertia
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.inertial = inertial
Namespace.addCategoryObject('typeBinding', 'inertial', inertial)


# Complex type {http://www.ros.org}box with content type EMPTY
class box (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.ros.org}box with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'box')
    _XSDLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 68, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute size uses Python identifier size
    __size = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'size'), 'size', '__httpwww_ros_org_box_size', pyxb.binding.datatypes.string, unicode_default='0 0 0')
    __size._DeclarationLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 69, 4)
    __size._UseLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 69, 4)
    
    size = property(__size.value, __size.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __size.name() : __size
    })
_module_typeBindings.box = box
Namespace.addCategoryObject('typeBinding', 'box', box)


# Complex type {http://www.ros.org}cylinder with content type EMPTY
class cylinder (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.ros.org}cylinder with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'cylinder')
    _XSDLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 73, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute radius uses Python identifier radius
    __radius = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'radius'), 'radius', '__httpwww_ros_org_cylinder_radius', pyxb.binding.datatypes.double, required=True)
    __radius._DeclarationLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 74, 4)
    __radius._UseLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 74, 4)
    
    radius = property(__radius.value, __radius.set, None, None)

    
    # Attribute length uses Python identifier length
    __length = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'length'), 'length', '__httpwww_ros_org_cylinder_length', pyxb.binding.datatypes.double, required=True)
    __length._DeclarationLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 75, 4)
    __length._UseLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 75, 4)
    
    length = property(__length.value, __length.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __radius.name() : __radius,
        __length.name() : __length
    })
_module_typeBindings.cylinder = cylinder
Namespace.addCategoryObject('typeBinding', 'cylinder', cylinder)


# Complex type {http://www.ros.org}sphere with content type EMPTY
class sphere (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.ros.org}sphere with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'sphere')
    _XSDLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 79, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute radius uses Python identifier radius
    __radius = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'radius'), 'radius', '__httpwww_ros_org_sphere_radius', pyxb.binding.datatypes.double, required=True)
    __radius._DeclarationLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 80, 4)
    __radius._UseLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 80, 4)
    
    radius = property(__radius.value, __radius.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __radius.name() : __radius
    })
_module_typeBindings.sphere = sphere
Namespace.addCategoryObject('typeBinding', 'sphere', sphere)


# Complex type {http://www.ros.org}mesh with content type EMPTY
class mesh (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.ros.org}mesh with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'mesh')
    _XSDLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 84, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute filename uses Python identifier filename
    __filename = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'filename'), 'filename', '__httpwww_ros_org_mesh_filename', pyxb.binding.datatypes.anyURI, required=True)
    __filename._DeclarationLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 85, 4)
    __filename._UseLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 85, 4)
    
    filename = property(__filename.value, __filename.set, None, None)

    
    # Attribute scale uses Python identifier scale
    __scale = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'scale'), 'scale', '__httpwww_ros_org_mesh_scale', pyxb.binding.datatypes.string, unicode_default='1 1 1')
    __scale._DeclarationLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 86, 4)
    __scale._UseLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 86, 4)
    
    scale = property(__scale.value, __scale.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __filename.name() : __filename,
        __scale.name() : __scale
    })
_module_typeBindings.mesh = mesh
Namespace.addCategoryObject('typeBinding', 'mesh', mesh)


# Complex type {http://www.ros.org}geometry with content type ELEMENT_ONLY
class geometry (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.ros.org}geometry with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'geometry')
    _XSDLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 90, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.ros.org}box uses Python identifier box
    __box = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'box'), 'box', '__httpwww_ros_org_geometry_httpwww_ros_orgbox', False, pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 92, 6), )

    
    box = property(__box.value, __box.set, None, None)

    
    # Element {http://www.ros.org}cylinder uses Python identifier cylinder
    __cylinder = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'cylinder'), 'cylinder', '__httpwww_ros_org_geometry_httpwww_ros_orgcylinder', False, pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 93, 6), )

    
    cylinder = property(__cylinder.value, __cylinder.set, None, None)

    
    # Element {http://www.ros.org}sphere uses Python identifier sphere
    __sphere = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'sphere'), 'sphere', '__httpwww_ros_org_geometry_httpwww_ros_orgsphere', False, pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 94, 6), )

    
    sphere = property(__sphere.value, __sphere.set, None, None)

    
    # Element {http://www.ros.org}mesh uses Python identifier mesh
    __mesh = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'mesh'), 'mesh', '__httpwww_ros_org_geometry_httpwww_ros_orgmesh', False, pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 95, 6), )

    
    mesh = property(__mesh.value, __mesh.set, None, None)

    _ElementMap.update({
        __box.name() : __box,
        __cylinder.name() : __cylinder,
        __sphere.name() : __sphere,
        __mesh.name() : __mesh
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.geometry = geometry
Namespace.addCategoryObject('typeBinding', 'geometry', geometry)


# Complex type {http://www.ros.org}texture with content type EMPTY
class texture (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.ros.org}texture with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'texture')
    _XSDLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 100, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute filename uses Python identifier filename
    __filename = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'filename'), 'filename', '__httpwww_ros_org_texture_filename', pyxb.binding.datatypes.anyURI)
    __filename._DeclarationLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 101, 4)
    __filename._UseLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 101, 4)
    
    filename = property(__filename.value, __filename.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __filename.name() : __filename
    })
_module_typeBindings.texture = texture
Namespace.addCategoryObject('typeBinding', 'texture', texture)


# Complex type {http://www.ros.org}material with content type ELEMENT_ONLY
class material (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.ros.org}material with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'material')
    _XSDLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 105, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.ros.org}color uses Python identifier color
    __color = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'color'), 'color', '__httpwww_ros_org_material_httpwww_ros_orgcolor', False, pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 107, 6), )

    
    color = property(__color.value, __color.set, None, None)

    
    # Element {http://www.ros.org}texture uses Python identifier texture
    __texture = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'texture'), 'texture', '__httpwww_ros_org_material_httpwww_ros_orgtexture', False, pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 108, 6), )

    
    texture = property(__texture.value, __texture.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpwww_ros_org_material_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 110, 4)
    __name._UseLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 110, 4)
    
    name = property(__name.value, __name.set, None, None)

    _ElementMap.update({
        __color.name() : __color,
        __texture.name() : __texture
    })
    _AttributeMap.update({
        __name.name() : __name
    })
_module_typeBindings.material = material
Namespace.addCategoryObject('typeBinding', 'material', material)


# Complex type {http://www.ros.org}material_global with content type ELEMENT_ONLY
class material_global (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.ros.org}material_global with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'material_global')
    _XSDLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 114, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.ros.org}color uses Python identifier color
    __color = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'color'), 'color', '__httpwww_ros_org_material_global_httpwww_ros_orgcolor', False, pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 116, 6), )

    
    color = property(__color.value, __color.set, None, None)

    
    # Element {http://www.ros.org}texture uses Python identifier texture
    __texture = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'texture'), 'texture', '__httpwww_ros_org_material_global_httpwww_ros_orgtexture', False, pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 117, 6), )

    
    texture = property(__texture.value, __texture.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpwww_ros_org_material_global_name', pyxb.binding.datatypes.string, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 119, 4)
    __name._UseLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 119, 4)
    
    name = property(__name.value, __name.set, None, None)

    _ElementMap.update({
        __color.name() : __color,
        __texture.name() : __texture
    })
    _AttributeMap.update({
        __name.name() : __name
    })
_module_typeBindings.material_global = material_global
Namespace.addCategoryObject('typeBinding', 'material_global', material_global)


# Complex type {http://www.ros.org}visual with content type ELEMENT_ONLY
class visual (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.ros.org}visual with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'visual')
    _XSDLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 124, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.ros.org}origin uses Python identifier origin
    __origin = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'origin'), 'origin', '__httpwww_ros_org_visual_httpwww_ros_orgorigin', False, pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 126, 6), )

    
    origin = property(__origin.value, __origin.set, None, None)

    
    # Element {http://www.ros.org}geometry uses Python identifier geometry
    __geometry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'geometry'), 'geometry', '__httpwww_ros_org_visual_httpwww_ros_orggeometry', False, pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 128, 6), )

    
    geometry = property(__geometry.value, __geometry.set, None, None)

    
    # Element {http://www.ros.org}material uses Python identifier material
    __material = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'material'), 'material', '__httpwww_ros_org_visual_httpwww_ros_orgmaterial', False, pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 130, 6), )

    
    material = property(__material.value, __material.set, None, None)

    _ElementMap.update({
        __origin.name() : __origin,
        __geometry.name() : __geometry,
        __material.name() : __material
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.visual = visual
Namespace.addCategoryObject('typeBinding', 'visual', visual)


# Complex type {http://www.ros.org}collision with content type ELEMENT_ONLY
class collision (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.ros.org}collision with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'collision')
    _XSDLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 136, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.ros.org}origin uses Python identifier origin
    __origin = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'origin'), 'origin', '__httpwww_ros_org_collision_httpwww_ros_orgorigin', False, pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 138, 6), )

    
    origin = property(__origin.value, __origin.set, None, None)

    
    # Element {http://www.ros.org}geometry uses Python identifier geometry
    __geometry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'geometry'), 'geometry', '__httpwww_ros_org_collision_httpwww_ros_orggeometry', False, pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 140, 6), )

    
    geometry = property(__geometry.value, __geometry.set, None, None)

    
    # Element {http://www.ros.org}verbose uses Python identifier verbose
    __verbose = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'verbose'), 'verbose', '__httpwww_ros_org_collision_httpwww_ros_orgverbose', False, pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 142, 6), )

    
    verbose = property(__verbose.value, __verbose.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpwww_ros_org_collision_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 146, 4)
    __name._UseLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 146, 4)
    
    name = property(__name.value, __name.set, None, None)

    _ElementMap.update({
        __origin.name() : __origin,
        __geometry.name() : __geometry,
        __verbose.name() : __verbose
    })
    _AttributeMap.update({
        __name.name() : __name
    })
_module_typeBindings.collision = collision
Namespace.addCategoryObject('typeBinding', 'collision', collision)


# Complex type {http://www.ros.org}link with content type ELEMENT_ONLY
class link (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.ros.org}link with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'link')
    _XSDLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 150, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.ros.org}inertial uses Python identifier inertial
    __inertial = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'inertial'), 'inertial', '__httpwww_ros_org_link_httpwww_ros_orginertial', True, pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 152, 6), )

    
    inertial = property(__inertial.value, __inertial.set, None, None)

    
    # Element {http://www.ros.org}visual uses Python identifier visual
    __visual = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'visual'), 'visual', '__httpwww_ros_org_link_httpwww_ros_orgvisual', True, pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 153, 6), )

    
    visual = property(__visual.value, __visual.set, None, None)

    
    # Element {http://www.ros.org}collision uses Python identifier collision
    __collision = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'collision'), 'collision', '__httpwww_ros_org_link_httpwww_ros_orgcollision', True, pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 154, 6), )

    
    collision = property(__collision.value, __collision.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpwww_ros_org_link_name', pyxb.binding.datatypes.string, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 156, 4)
    __name._UseLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 156, 4)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__httpwww_ros_org_link_type', pyxb.binding.datatypes.string)
    __type._DeclarationLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 159, 4)
    __type._UseLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 159, 4)
    
    type = property(__type.value, __type.set, None, None)

    _ElementMap.update({
        __inertial.name() : __inertial,
        __visual.name() : __visual,
        __collision.name() : __collision
    })
    _AttributeMap.update({
        __name.name() : __name,
        __type.name() : __type
    })
_module_typeBindings.link = link
Namespace.addCategoryObject('typeBinding', 'link', link)


# Complex type {http://www.ros.org}parent with content type EMPTY
class parent (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.ros.org}parent with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'parent')
    _XSDLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 164, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute link uses Python identifier link
    __link = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'link'), 'link', '__httpwww_ros_org_parent_link', pyxb.binding.datatypes.string, required=True)
    __link._DeclarationLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 165, 4)
    __link._UseLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 165, 4)
    
    link = property(__link.value, __link.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __link.name() : __link
    })
_module_typeBindings.parent = parent
Namespace.addCategoryObject('typeBinding', 'parent', parent)


# Complex type {http://www.ros.org}child with content type EMPTY
class child (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.ros.org}child with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'child')
    _XSDLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 169, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute link uses Python identifier link
    __link = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'link'), 'link', '__httpwww_ros_org_child_link', pyxb.binding.datatypes.string, required=True)
    __link._DeclarationLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 170, 4)
    __link._UseLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 170, 4)
    
    link = property(__link.value, __link.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __link.name() : __link
    })
_module_typeBindings.child = child
Namespace.addCategoryObject('typeBinding', 'child', child)


# Complex type {http://www.ros.org}axis with content type EMPTY
class axis (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.ros.org}axis with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'axis')
    _XSDLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 174, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute xyz uses Python identifier xyz
    __xyz = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'xyz'), 'xyz', '__httpwww_ros_org_axis_xyz', pyxb.binding.datatypes.string, unicode_default='1 0 0')
    __xyz._DeclarationLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 175, 4)
    __xyz._UseLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 175, 4)
    
    xyz = property(__xyz.value, __xyz.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __xyz.name() : __xyz
    })
_module_typeBindings.axis = axis
Namespace.addCategoryObject('typeBinding', 'axis', axis)


# Complex type {http://www.ros.org}calibration with content type EMPTY
class calibration (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.ros.org}calibration with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'calibration')
    _XSDLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 179, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute reference_position uses Python identifier reference_position
    __reference_position = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'reference_position'), 'reference_position', '__httpwww_ros_org_calibration_reference_position', pyxb.binding.datatypes.double)
    __reference_position._DeclarationLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 180, 4)
    __reference_position._UseLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 180, 4)
    
    reference_position = property(__reference_position.value, __reference_position.set, None, None)

    
    # Attribute rising uses Python identifier rising
    __rising = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'rising'), 'rising', '__httpwww_ros_org_calibration_rising', pyxb.binding.datatypes.double)
    __rising._DeclarationLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 181, 4)
    __rising._UseLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 181, 4)
    
    rising = property(__rising.value, __rising.set, None, None)

    
    # Attribute falling uses Python identifier falling
    __falling = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'falling'), 'falling', '__httpwww_ros_org_calibration_falling', pyxb.binding.datatypes.double)
    __falling._DeclarationLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 182, 4)
    __falling._UseLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 182, 4)
    
    falling = property(__falling.value, __falling.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __reference_position.name() : __reference_position,
        __rising.name() : __rising,
        __falling.name() : __falling
    })
_module_typeBindings.calibration = calibration
Namespace.addCategoryObject('typeBinding', 'calibration', calibration)


# Complex type {http://www.ros.org}dynamics with content type EMPTY
class dynamics (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.ros.org}dynamics with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'dynamics')
    _XSDLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 186, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute damping uses Python identifier damping
    __damping = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'damping'), 'damping', '__httpwww_ros_org_dynamics_damping', pyxb.binding.datatypes.double, unicode_default='0')
    __damping._DeclarationLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 187, 4)
    __damping._UseLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 187, 4)
    
    damping = property(__damping.value, __damping.set, None, None)

    
    # Attribute friction uses Python identifier friction
    __friction = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'friction'), 'friction', '__httpwww_ros_org_dynamics_friction', pyxb.binding.datatypes.double, unicode_default='0')
    __friction._DeclarationLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 188, 4)
    __friction._UseLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 188, 4)
    
    friction = property(__friction.value, __friction.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __damping.name() : __damping,
        __friction.name() : __friction
    })
_module_typeBindings.dynamics = dynamics
Namespace.addCategoryObject('typeBinding', 'dynamics', dynamics)


# Complex type {http://www.ros.org}limit with content type EMPTY
class limit (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.ros.org}limit with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'limit')
    _XSDLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 192, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute lower uses Python identifier lower
    __lower = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'lower'), 'lower', '__httpwww_ros_org_limit_lower', pyxb.binding.datatypes.double, unicode_default='0')
    __lower._DeclarationLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 193, 4)
    __lower._UseLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 193, 4)
    
    lower = property(__lower.value, __lower.set, None, None)

    
    # Attribute upper uses Python identifier upper
    __upper = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'upper'), 'upper', '__httpwww_ros_org_limit_upper', pyxb.binding.datatypes.double, unicode_default='0')
    __upper._DeclarationLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 194, 4)
    __upper._UseLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 194, 4)
    
    upper = property(__upper.value, __upper.set, None, None)

    
    # Attribute effort uses Python identifier effort
    __effort = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'effort'), 'effort', '__httpwww_ros_org_limit_effort', pyxb.binding.datatypes.double, unicode_default='0')
    __effort._DeclarationLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 195, 4)
    __effort._UseLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 195, 4)
    
    effort = property(__effort.value, __effort.set, None, None)

    
    # Attribute velocity uses Python identifier velocity
    __velocity = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'velocity'), 'velocity', '__httpwww_ros_org_limit_velocity', pyxb.binding.datatypes.double, unicode_default='0')
    __velocity._DeclarationLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 196, 4)
    __velocity._UseLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 196, 4)
    
    velocity = property(__velocity.value, __velocity.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __lower.name() : __lower,
        __upper.name() : __upper,
        __effort.name() : __effort,
        __velocity.name() : __velocity
    })
_module_typeBindings.limit = limit
Namespace.addCategoryObject('typeBinding', 'limit', limit)


# Complex type {http://www.ros.org}safety_controller with content type EMPTY
class safety_controller (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.ros.org}safety_controller with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'safety_controller')
    _XSDLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 200, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute soft_lower_limit uses Python identifier soft_lower_limit
    __soft_lower_limit = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'soft_lower_limit'), 'soft_lower_limit', '__httpwww_ros_org_safety_controller_soft_lower_limit', pyxb.binding.datatypes.double, unicode_default='0')
    __soft_lower_limit._DeclarationLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 201, 4)
    __soft_lower_limit._UseLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 201, 4)
    
    soft_lower_limit = property(__soft_lower_limit.value, __soft_lower_limit.set, None, None)

    
    # Attribute soft_upper_limit uses Python identifier soft_upper_limit
    __soft_upper_limit = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'soft_upper_limit'), 'soft_upper_limit', '__httpwww_ros_org_safety_controller_soft_upper_limit', pyxb.binding.datatypes.double, unicode_default='0')
    __soft_upper_limit._DeclarationLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 202, 4)
    __soft_upper_limit._UseLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 202, 4)
    
    soft_upper_limit = property(__soft_upper_limit.value, __soft_upper_limit.set, None, None)

    
    # Attribute k_position uses Python identifier k_position
    __k_position = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'k_position'), 'k_position', '__httpwww_ros_org_safety_controller_k_position', pyxb.binding.datatypes.double, unicode_default='0')
    __k_position._DeclarationLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 203, 4)
    __k_position._UseLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 203, 4)
    
    k_position = property(__k_position.value, __k_position.set, None, None)

    
    # Attribute k_velocity uses Python identifier k_velocity
    __k_velocity = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'k_velocity'), 'k_velocity', '__httpwww_ros_org_safety_controller_k_velocity', pyxb.binding.datatypes.double, required=True)
    __k_velocity._DeclarationLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 204, 4)
    __k_velocity._UseLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 204, 4)
    
    k_velocity = property(__k_velocity.value, __k_velocity.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __soft_lower_limit.name() : __soft_lower_limit,
        __soft_upper_limit.name() : __soft_upper_limit,
        __k_position.name() : __k_position,
        __k_velocity.name() : __k_velocity
    })
_module_typeBindings.safety_controller = safety_controller
Namespace.addCategoryObject('typeBinding', 'safety_controller', safety_controller)


# Complex type {http://www.ros.org}mimic with content type EMPTY
class mimic (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.ros.org}mimic with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'mimic')
    _XSDLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 208, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute joint uses Python identifier joint
    __joint = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'joint'), 'joint', '__httpwww_ros_org_mimic_joint', pyxb.binding.datatypes.string, required=True)
    __joint._DeclarationLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 209, 4)
    __joint._UseLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 209, 4)
    
    joint = property(__joint.value, __joint.set, None, None)

    
    # Attribute multiplier uses Python identifier multiplier
    __multiplier = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'multiplier'), 'multiplier', '__httpwww_ros_org_mimic_multiplier', pyxb.binding.datatypes.double, unicode_default='1')
    __multiplier._DeclarationLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 210, 4)
    __multiplier._UseLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 210, 4)
    
    multiplier = property(__multiplier.value, __multiplier.set, None, None)

    
    # Attribute offset uses Python identifier offset
    __offset = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'offset'), 'offset', '__httpwww_ros_org_mimic_offset', pyxb.binding.datatypes.double, unicode_default='0')
    __offset._DeclarationLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 211, 4)
    __offset._UseLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 211, 4)
    
    offset = property(__offset.value, __offset.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __joint.name() : __joint,
        __multiplier.name() : __multiplier,
        __offset.name() : __offset
    })
_module_typeBindings.mimic = mimic
Namespace.addCategoryObject('typeBinding', 'mimic', mimic)


# Complex type {http://www.ros.org}actuator_transmission with content type EMPTY
class actuator_transmission (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.ros.org}actuator_transmission with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'actuator_transmission')
    _XSDLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 215, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute mechanicalReduction uses Python identifier mechanicalReduction
    __mechanicalReduction = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'mechanicalReduction'), 'mechanicalReduction', '__httpwww_ros_org_actuator_transmission_mechanicalReduction', pyxb.binding.datatypes.double, required=True)
    __mechanicalReduction._DeclarationLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 216, 4)
    __mechanicalReduction._UseLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 216, 4)
    
    mechanicalReduction = property(__mechanicalReduction.value, __mechanicalReduction.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpwww_ros_org_actuator_transmission_name', pyxb.binding.datatypes.string, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 217, 4)
    __name._UseLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 217, 4)
    
    name = property(__name.value, __name.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __mechanicalReduction.name() : __mechanicalReduction,
        __name.name() : __name
    })
_module_typeBindings.actuator_transmission = actuator_transmission
Namespace.addCategoryObject('typeBinding', 'actuator_transmission', actuator_transmission)


# Complex type {http://www.ros.org}gap_joint_transmission with content type EMPTY
class gap_joint_transmission (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.ros.org}gap_joint_transmission with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'gap_joint_transmission')
    _XSDLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 221, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute L0 uses Python identifier L0
    __L0 = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'L0'), 'L0', '__httpwww_ros_org_gap_joint_transmission_L0', pyxb.binding.datatypes.double, required=True)
    __L0._DeclarationLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 222, 4)
    __L0._UseLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 222, 4)
    
    L0 = property(__L0.value, __L0.set, None, None)

    
    # Attribute a uses Python identifier a
    __a = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'a'), 'a', '__httpwww_ros_org_gap_joint_transmission_a', pyxb.binding.datatypes.double, required=True)
    __a._DeclarationLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 223, 4)
    __a._UseLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 223, 4)
    
    a = property(__a.value, __a.set, None, None)

    
    # Attribute b uses Python identifier b
    __b = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'b'), 'b', '__httpwww_ros_org_gap_joint_transmission_b', pyxb.binding.datatypes.double, required=True)
    __b._DeclarationLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 224, 4)
    __b._UseLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 224, 4)
    
    b = property(__b.value, __b.set, None, None)

    
    # Attribute gear_ratio uses Python identifier gear_ratio
    __gear_ratio = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'gear_ratio'), 'gear_ratio', '__httpwww_ros_org_gap_joint_transmission_gear_ratio', pyxb.binding.datatypes.double, required=True)
    __gear_ratio._DeclarationLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 225, 4)
    __gear_ratio._UseLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 225, 4)
    
    gear_ratio = property(__gear_ratio.value, __gear_ratio.set, None, None)

    
    # Attribute h uses Python identifier h
    __h = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'h'), 'h', '__httpwww_ros_org_gap_joint_transmission_h', pyxb.binding.datatypes.double, required=True)
    __h._DeclarationLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 226, 4)
    __h._UseLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 226, 4)
    
    h = property(__h.value, __h.set, None, None)

    
    # Attribute mechanical_reduction uses Python identifier mechanical_reduction
    __mechanical_reduction = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'mechanical_reduction'), 'mechanical_reduction', '__httpwww_ros_org_gap_joint_transmission_mechanical_reduction', pyxb.binding.datatypes.double, required=True)
    __mechanical_reduction._DeclarationLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 227, 4)
    __mechanical_reduction._UseLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 227, 4)
    
    mechanical_reduction = property(__mechanical_reduction.value, __mechanical_reduction.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpwww_ros_org_gap_joint_transmission_name', pyxb.binding.datatypes.string, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 228, 4)
    __name._UseLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 228, 4)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute phi0 uses Python identifier phi0
    __phi0 = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'phi0'), 'phi0', '__httpwww_ros_org_gap_joint_transmission_phi0', pyxb.binding.datatypes.double, required=True)
    __phi0._DeclarationLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 229, 4)
    __phi0._UseLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 229, 4)
    
    phi0 = property(__phi0.value, __phi0.set, None, None)

    
    # Attribute r uses Python identifier r
    __r = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'r'), 'r', '__httpwww_ros_org_gap_joint_transmission_r', pyxb.binding.datatypes.double, required=True)
    __r._DeclarationLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 230, 4)
    __r._UseLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 230, 4)
    
    r = property(__r.value, __r.set, None, None)

    
    # Attribute screw_reduction uses Python identifier screw_reduction
    __screw_reduction = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'screw_reduction'), 'screw_reduction', '__httpwww_ros_org_gap_joint_transmission_screw_reduction', pyxb.binding.datatypes.double, required=True)
    __screw_reduction._DeclarationLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 231, 4)
    __screw_reduction._UseLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 231, 4)
    
    screw_reduction = property(__screw_reduction.value, __screw_reduction.set, None, None)

    
    # Attribute t0 uses Python identifier t0
    __t0 = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 't0'), 't0', '__httpwww_ros_org_gap_joint_transmission_t0', pyxb.binding.datatypes.double, required=True)
    __t0._DeclarationLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 232, 4)
    __t0._UseLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 232, 4)
    
    t0 = property(__t0.value, __t0.set, None, None)

    
    # Attribute theta0 uses Python identifier theta0
    __theta0 = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'theta0'), 'theta0', '__httpwww_ros_org_gap_joint_transmission_theta0', pyxb.binding.datatypes.double, required=True)
    __theta0._DeclarationLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 233, 4)
    __theta0._UseLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 233, 4)
    
    theta0 = property(__theta0.value, __theta0.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __L0.name() : __L0,
        __a.name() : __a,
        __b.name() : __b,
        __gear_ratio.name() : __gear_ratio,
        __h.name() : __h,
        __mechanical_reduction.name() : __mechanical_reduction,
        __name.name() : __name,
        __phi0.name() : __phi0,
        __r.name() : __r,
        __screw_reduction.name() : __screw_reduction,
        __t0.name() : __t0,
        __theta0.name() : __theta0
    })
_module_typeBindings.gap_joint_transmission = gap_joint_transmission
Namespace.addCategoryObject('typeBinding', 'gap_joint_transmission', gap_joint_transmission)


# Complex type {http://www.ros.org}passive_joint_transmission with content type EMPTY
class passive_joint_transmission (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.ros.org}passive_joint_transmission with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'passive_joint_transmission')
    _XSDLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 237, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpwww_ros_org_passive_joint_transmission_name', pyxb.binding.datatypes.string, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 238, 4)
    __name._UseLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 238, 4)
    
    name = property(__name.value, __name.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __name.name() : __name
    })
_module_typeBindings.passive_joint_transmission = passive_joint_transmission
Namespace.addCategoryObject('typeBinding', 'passive_joint_transmission', passive_joint_transmission)


# Complex type {http://www.ros.org}transmission with content type ELEMENT_ONLY
class transmission (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.ros.org}transmission with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'transmission')
    _XSDLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 242, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.ros.org}leftActuator uses Python identifier leftActuator
    __leftActuator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'leftActuator'), 'leftActuator', '__httpwww_ros_org_transmission_httpwww_ros_orgleftActuator', True, pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 244, 6), )

    
    leftActuator = property(__leftActuator.value, __leftActuator.set, None, None)

    
    # Element {http://www.ros.org}rightActuator uses Python identifier rightActuator
    __rightActuator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'rightActuator'), 'rightActuator', '__httpwww_ros_org_transmission_httpwww_ros_orgrightActuator', True, pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 246, 6), )

    
    rightActuator = property(__rightActuator.value, __rightActuator.set, None, None)

    
    # Element {http://www.ros.org}flexJoint uses Python identifier flexJoint
    __flexJoint = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'flexJoint'), 'flexJoint', '__httpwww_ros_org_transmission_httpwww_ros_orgflexJoint', True, pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 248, 6), )

    
    flexJoint = property(__flexJoint.value, __flexJoint.set, None, None)

    
    # Element {http://www.ros.org}rollJoint uses Python identifier rollJoint
    __rollJoint = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'rollJoint'), 'rollJoint', '__httpwww_ros_org_transmission_httpwww_ros_orgrollJoint', True, pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 250, 6), )

    
    rollJoint = property(__rollJoint.value, __rollJoint.set, None, None)

    
    # Element {http://www.ros.org}gap_joint uses Python identifier gap_joint
    __gap_joint = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'gap_joint'), 'gap_joint', '__httpwww_ros_org_transmission_httpwww_ros_orggap_joint', True, pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 252, 6), )

    
    gap_joint = property(__gap_joint.value, __gap_joint.set, None, None)

    
    # Element {http://www.ros.org}passive_joint uses Python identifier passive_joint
    __passive_joint = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'passive_joint'), 'passive_joint', '__httpwww_ros_org_transmission_httpwww_ros_orgpassive_joint', True, pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 254, 6), )

    
    passive_joint = property(__passive_joint.value, __passive_joint.set, None, None)

    
    # Element {http://www.ros.org}use_simulated_gripper_joint uses Python identifier use_simulated_gripper_joint
    __use_simulated_gripper_joint = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'use_simulated_gripper_joint'), 'use_simulated_gripper_joint', '__httpwww_ros_org_transmission_httpwww_ros_orguse_simulated_gripper_joint', True, pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 256, 6), )

    
    use_simulated_gripper_joint = property(__use_simulated_gripper_joint.value, __use_simulated_gripper_joint.set, None, None)

    
    # Element {http://www.ros.org}mechanicalReduction uses Python identifier mechanicalReduction
    __mechanicalReduction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'mechanicalReduction'), 'mechanicalReduction', '__httpwww_ros_org_transmission_httpwww_ros_orgmechanicalReduction', True, pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 260, 6), )

    
    mechanicalReduction = property(__mechanicalReduction.value, __mechanicalReduction.set, None, None)

    
    # Element {http://www.ros.org}actuator uses Python identifier actuator
    __actuator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'actuator'), 'actuator', '__httpwww_ros_org_transmission_httpwww_ros_orgactuator', True, pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 263, 6), )

    
    actuator = property(__actuator.value, __actuator.set, None, None)

    
    # Element {http://www.ros.org}joint uses Python identifier joint
    __joint = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'joint'), 'joint', '__httpwww_ros_org_transmission_httpwww_ros_orgjoint', True, pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 264, 6), )

    
    joint = property(__joint.value, __joint.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpwww_ros_org_transmission_name', pyxb.binding.datatypes.string, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 266, 4)
    __name._UseLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 266, 4)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__httpwww_ros_org_transmission_type', pyxb.binding.datatypes.string, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 267, 4)
    __type._UseLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 267, 4)
    
    type = property(__type.value, __type.set, None, None)

    _ElementMap.update({
        __leftActuator.name() : __leftActuator,
        __rightActuator.name() : __rightActuator,
        __flexJoint.name() : __flexJoint,
        __rollJoint.name() : __rollJoint,
        __gap_joint.name() : __gap_joint,
        __passive_joint.name() : __passive_joint,
        __use_simulated_gripper_joint.name() : __use_simulated_gripper_joint,
        __mechanicalReduction.name() : __mechanicalReduction,
        __actuator.name() : __actuator,
        __joint.name() : __joint
    })
    _AttributeMap.update({
        __name.name() : __name,
        __type.name() : __type
    })
_module_typeBindings.transmission = transmission
Namespace.addCategoryObject('typeBinding', 'transmission', transmission)


# Complex type [anonymous] with content type EMPTY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 257, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON = CTD_ANON


# Complex type {http://www.ros.org}joint with content type ELEMENT_ONLY
class joint (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.ros.org}joint with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'joint')
    _XSDLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 271, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.ros.org}origin uses Python identifier origin
    __origin = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'origin'), 'origin', '__httpwww_ros_org_joint_httpwww_ros_orgorigin', False, pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 273, 6), )

    
    origin = property(__origin.value, __origin.set, None, None)

    
    # Element {http://www.ros.org}parent uses Python identifier parent
    __parent = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'parent'), 'parent', '__httpwww_ros_org_joint_httpwww_ros_orgparent', False, pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 275, 6), )

    
    parent = property(__parent.value, __parent.set, None, None)

    
    # Element {http://www.ros.org}child uses Python identifier child
    __child = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'child'), 'child', '__httpwww_ros_org_joint_httpwww_ros_orgchild', False, pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 277, 6), )

    
    child = property(__child.value, __child.set, None, None)

    
    # Element {http://www.ros.org}axis uses Python identifier axis
    __axis = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'axis'), 'axis', '__httpwww_ros_org_joint_httpwww_ros_orgaxis', False, pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 279, 6), )

    
    axis = property(__axis.value, __axis.set, None, None)

    
    # Element {http://www.ros.org}calibration uses Python identifier calibration
    __calibration = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'calibration'), 'calibration', '__httpwww_ros_org_joint_httpwww_ros_orgcalibration', False, pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 281, 6), )

    
    calibration = property(__calibration.value, __calibration.set, None, None)

    
    # Element {http://www.ros.org}dynamics uses Python identifier dynamics
    __dynamics = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'dynamics'), 'dynamics', '__httpwww_ros_org_joint_httpwww_ros_orgdynamics', False, pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 283, 6), )

    
    dynamics = property(__dynamics.value, __dynamics.set, None, None)

    
    # Element {http://www.ros.org}limit uses Python identifier limit
    __limit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'limit'), 'limit', '__httpwww_ros_org_joint_httpwww_ros_orglimit', False, pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 285, 6), )

    
    limit = property(__limit.value, __limit.set, None, None)

    
    # Element {http://www.ros.org}safety_controller uses Python identifier safety_controller
    __safety_controller = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'safety_controller'), 'safety_controller', '__httpwww_ros_org_joint_httpwww_ros_orgsafety_controller', False, pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 287, 6), )

    
    safety_controller = property(__safety_controller.value, __safety_controller.set, None, None)

    
    # Element {http://www.ros.org}mimic uses Python identifier mimic
    __mimic = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'mimic'), 'mimic', '__httpwww_ros_org_joint_httpwww_ros_orgmimic', False, pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 289, 6), )

    
    mimic = property(__mimic.value, __mimic.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpwww_ros_org_joint_name', pyxb.binding.datatypes.string, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 292, 4)
    __name._UseLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 292, 4)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__httpwww_ros_org_joint_type', pyxb.binding.datatypes.string, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 293, 4)
    __type._UseLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 293, 4)
    
    type = property(__type.value, __type.set, None, None)

    _ElementMap.update({
        __origin.name() : __origin,
        __parent.name() : __parent,
        __child.name() : __child,
        __axis.name() : __axis,
        __calibration.name() : __calibration,
        __dynamics.name() : __dynamics,
        __limit.name() : __limit,
        __safety_controller.name() : __safety_controller,
        __mimic.name() : __mimic
    })
    _AttributeMap.update({
        __name.name() : __name,
        __type.name() : __type
    })
_module_typeBindings.joint = joint
Namespace.addCategoryObject('typeBinding', 'joint', joint)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 298, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.ros.org}joint uses Python identifier joint
    __joint = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'joint'), 'joint', '__httpwww_ros_org_CTD_ANON__httpwww_ros_orgjoint', True, pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 300, 1), )

    
    joint = property(__joint.value, __joint.set, None, None)

    
    # Element {http://www.ros.org}link uses Python identifier link
    __link = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'link'), 'link', '__httpwww_ros_org_CTD_ANON__httpwww_ros_orglink', True, pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 302, 1), )

    
    link = property(__link.value, __link.set, None, None)

    
    # Element {http://www.ros.org}material uses Python identifier material
    __material = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'material'), 'material', '__httpwww_ros_org_CTD_ANON__httpwww_ros_orgmaterial', True, pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 306, 1), )

    
    material = property(__material.value, __material.set, None, None)

    
    # Element {http://www.ros.org}transmission uses Python identifier transmission
    __transmission = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'transmission'), 'transmission', '__httpwww_ros_org_CTD_ANON__httpwww_ros_orgtransmission', True, pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 310, 1), )

    
    transmission = property(__transmission.value, __transmission.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpwww_ros_org_CTD_ANON__name', pyxb.binding.datatypes.string, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 315, 6)
    __name._UseLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 315, 6)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'version'), 'version', '__httpwww_ros_org_CTD_ANON__version', pyxb.binding.datatypes.string, unicode_default='1.0')
    __version._DeclarationLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 318, 6)
    __version._UseLocation = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 318, 6)
    
    version = property(__version.value, __version.set, None, None)

    _ElementMap.update({
        __joint.name() : __joint,
        __link.name() : __link,
        __material.name() : __material,
        __transmission.name() : __transmission
    })
    _AttributeMap.update({
        __name.name() : __name,
        __version.name() : __version
    })
_module_typeBindings.CTD_ANON_ = CTD_ANON_


robot = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'robot'), CTD_ANON_, location=pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 297, 2))
Namespace.addCategoryObject('elementBinding', robot.name().localName(), robot)



inertial._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'origin'), pose, scope=inertial, location=pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 58, 6)))

inertial._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'mass'), mass, scope=inertial, location=pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 60, 6)))

inertial._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'inertia'), inertia, scope=inertial, location=pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 62, 6)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 58, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(inertial._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'origin')), pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 58, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 60, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(inertial._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'mass')), pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 60, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 62, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(inertial._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'inertia')), pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 62, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 58, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 60, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 62, 6))
    counters.add(cc_2)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_())
    sub_automata.append(_BuildAutomaton_2())
    sub_automata.append(_BuildAutomaton_3())
    final_update = set()
    symbol = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 57, 4)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
inertial._Automaton = _BuildAutomaton()




geometry._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'box'), box, scope=geometry, location=pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 92, 6)))

geometry._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'cylinder'), cylinder, scope=geometry, location=pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 93, 6)))

geometry._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'sphere'), sphere, scope=geometry, location=pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 94, 6)))

geometry._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'mesh'), mesh, scope=geometry, location=pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 95, 6)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(geometry._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'box')), pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 92, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(geometry._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'cylinder')), pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 93, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(geometry._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'sphere')), pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 94, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(geometry._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'mesh')), pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 95, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
geometry._Automaton = _BuildAutomaton_4()




material._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'color'), color, scope=material, location=pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 107, 6)))

material._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'texture'), texture, scope=material, location=pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 108, 6)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 107, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 108, 6))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(material._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'color')), pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 107, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(material._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'texture')), pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 108, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
material._Automaton = _BuildAutomaton_5()




material_global._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'color'), color, scope=material_global, location=pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 116, 6)))

material_global._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'texture'), texture, scope=material_global, location=pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 117, 6)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 116, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 117, 6))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(material_global._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'color')), pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 116, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(material_global._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'texture')), pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 117, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
material_global._Automaton = _BuildAutomaton_6()




visual._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'origin'), pose, scope=visual, location=pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 126, 6)))

visual._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'geometry'), geometry, scope=visual, location=pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 128, 6)))

visual._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'material'), material, scope=visual, location=pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 130, 6)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 126, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 130, 6))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(visual._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'origin')), pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 126, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(visual._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'geometry')), pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 128, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(visual._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'material')), pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 130, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
visual._Automaton = _BuildAutomaton_7()




collision._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'origin'), pose, scope=collision, location=pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 138, 6)))

collision._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'geometry'), geometry, scope=collision, location=pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 140, 6)))

collision._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'verbose'), verbose, scope=collision, location=pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 142, 6)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 138, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 142, 6))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(collision._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'origin')), pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 138, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(collision._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'geometry')), pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 140, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(collision._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'verbose')), pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 142, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
collision._Automaton = _BuildAutomaton_8()




link._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'inertial'), inertial, scope=link, location=pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 152, 6)))

link._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'visual'), visual, scope=link, location=pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 153, 6)))

link._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'collision'), collision, scope=link, location=pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 154, 6)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 151, 4))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(link._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'inertial')), pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 152, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(link._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'visual')), pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 153, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(link._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'collision')), pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 154, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
link._Automaton = _BuildAutomaton_9()




transmission._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'leftActuator'), actuator_transmission, scope=transmission, location=pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 244, 6)))

transmission._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'rightActuator'), actuator_transmission, scope=transmission, location=pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 246, 6)))

transmission._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'flexJoint'), actuator_transmission, scope=transmission, location=pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 248, 6)))

transmission._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'rollJoint'), actuator_transmission, scope=transmission, location=pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 250, 6)))

transmission._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'gap_joint'), gap_joint_transmission, scope=transmission, location=pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 252, 6)))

transmission._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'passive_joint'), passive_joint_transmission, scope=transmission, location=pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 254, 6)))

transmission._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'use_simulated_gripper_joint'), CTD_ANON, scope=transmission, location=pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 256, 6)))

transmission._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'mechanicalReduction'), pyxb.binding.datatypes.double, scope=transmission, location=pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 260, 6)))

transmission._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'actuator'), name, scope=transmission, location=pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 263, 6)))

transmission._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'joint'), name, scope=transmission, location=pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 264, 6)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 243, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 244, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 246, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 248, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 250, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 252, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 254, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 256, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 260, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 263, 6))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 264, 6))
    counters.add(cc_10)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(transmission._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'leftActuator')), pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 244, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(transmission._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'rightActuator')), pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 246, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(transmission._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'flexJoint')), pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 248, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(transmission._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'rollJoint')), pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 250, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(transmission._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'gap_joint')), pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 252, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(transmission._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'passive_joint')), pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 254, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(transmission._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'use_simulated_gripper_joint')), pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 256, 6))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(transmission._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'mechanicalReduction')), pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 260, 6))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(transmission._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'actuator')), pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 263, 6))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(transmission._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'joint')), pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 264, 6))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_10, True) ]))
    st_9._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
transmission._Automaton = _BuildAutomaton_10()




joint._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'origin'), pose, scope=joint, location=pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 273, 6)))

joint._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'parent'), parent, scope=joint, location=pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 275, 6)))

joint._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'child'), child, scope=joint, location=pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 277, 6)))

joint._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'axis'), axis, scope=joint, location=pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 279, 6)))

joint._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'calibration'), calibration, scope=joint, location=pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 281, 6)))

joint._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'dynamics'), dynamics, scope=joint, location=pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 283, 6)))

joint._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'limit'), limit, scope=joint, location=pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 285, 6)))

joint._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'safety_controller'), safety_controller, scope=joint, location=pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 287, 6)))

joint._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'mimic'), mimic, scope=joint, location=pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 289, 6)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 273, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(joint._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'origin')), pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 273, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(joint._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'parent')), pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 275, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=st_0)

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(joint._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'child')), pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 277, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=st_0)

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 279, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(joint._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'axis')), pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 279, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 281, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(joint._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'calibration')), pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 281, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 283, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(joint._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'dynamics')), pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 283, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 285, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(joint._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'limit')), pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 285, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_19 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 287, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(joint._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'safety_controller')), pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 287, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_20 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_20
    del _BuildAutomaton_20
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 289, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(joint._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'mimic')), pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 289, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 273, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 279, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 281, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 283, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 285, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 287, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 289, 6))
    counters.add(cc_6)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_12())
    sub_automata.append(_BuildAutomaton_13())
    sub_automata.append(_BuildAutomaton_14())
    sub_automata.append(_BuildAutomaton_15())
    sub_automata.append(_BuildAutomaton_16())
    sub_automata.append(_BuildAutomaton_17())
    sub_automata.append(_BuildAutomaton_18())
    sub_automata.append(_BuildAutomaton_19())
    sub_automata.append(_BuildAutomaton_20())
    final_update = set()
    symbol = pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 272, 4)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
joint._Automaton = _BuildAutomaton_11()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'joint'), joint, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 300, 1)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'link'), link, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 302, 1)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'material'), material_global, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 306, 1)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'transmission'), transmission, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 310, 1)))

def _BuildAutomaton_21 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_21
    del _BuildAutomaton_21
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 299, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 300, 1))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 302, 1))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 306, 1))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 310, 1))
    counters.add(cc_4)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'joint')), pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 300, 1))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'link')), pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 302, 1))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'material')), pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 306, 1))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'transmission')), pyxb.utils.utility.Location('/workspaces/urdf2/xsdFile/urdf_modified.xsd', 310, 1))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_21()

