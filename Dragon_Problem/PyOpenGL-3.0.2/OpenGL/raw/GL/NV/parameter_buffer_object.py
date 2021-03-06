'''Autogenerated by get_gl_extensions script, do not edit!'''
from OpenGL import platform as _p, constants as _cs, arrays
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_NV_parameter_buffer_object'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_NV_parameter_buffer_object',False)
_p.unpack_constants( """GL_MAX_PROGRAM_PARAMETER_BUFFER_BINDINGS_NV 0x8DA0
GL_MAX_PROGRAM_PARAMETER_BUFFER_SIZE_NV 0x8DA1
GL_VERTEX_PROGRAM_PARAMETER_BUFFER_NV 0x8DA2
GL_GEOMETRY_PROGRAM_PARAMETER_BUFFER_NV 0x8DA3
GL_FRAGMENT_PROGRAM_PARAMETER_BUFFER_NV 0x8DA4""", globals())
glget.addGLGetConstant( GL_VERTEX_PROGRAM_PARAMETER_BUFFER_NV, (1,) )
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint,_cs.GLuint,_cs.GLsizei,arrays.GLfloatArray)
def glProgramBufferParametersfvNV( target,buffer,index,count,params ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint,_cs.GLuint,_cs.GLsizei,arrays.GLintArray)
def glProgramBufferParametersIivNV( target,buffer,index,count,params ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint,_cs.GLuint,_cs.GLsizei,arrays.GLuintArray)
def glProgramBufferParametersIuivNV( target,buffer,index,count,params ):pass


def glInitParameterBufferObjectNV():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )
