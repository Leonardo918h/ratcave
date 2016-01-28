from __future__ import absolute_import

from os.path import join, split
from math import ceil, log

from pyglet.window import Window as PygletWindow
import pyglet.gl as gl

from .camera import Camera
from .shader import Shader
from .mesh import fullscreen_quad
from .utils import gl as ugl

shader_path = join(split(__file__)[0], 'shaders')


# General, Normal Shader
genShader = Shader(open(join(shader_path, 'combShader.vert')).read(),
                   open(join(shader_path, 'combShader.frag')).read())

shadowShader = Shader(open(join(shader_path, 'shadowShader.vert')).read(),
                      open(join(shader_path, 'shadowShader.frag')).read())

aaShader = Shader(open(join(shader_path, 'antialiasShader.vert')).read(),
                  open(join(shader_path, 'antialiasShader.frag')).read())

drawstyle = {'fill':gl.GL_TRIANGLES, 'line':gl.GL_LINE_LOOP, 'point':gl.GL_POINTS}


class Window(PygletWindow):
    
    def __init__(self, *args, **kwargs):
    
        # Set default Window values for making sure Psychopy windows work with it.
        super(Window, self).__init__(*args, **kwargs)

        self.fbos = {'shadow': ugl.create_fbo(gl.GL_TEXTURE_2D, texture_size, texture_size, texture_slot=5, color=False, depth=True),
                     'vrshadow': ugl.create_fbo(gl.GL_TEXTURE_2D, texture_size, texture_size, texture_slot=6, color=False, depth=True),
                     'cube': ugl.create_fbo(gl.GL_TEXTURE_CUBE_MAP, texture_size*2, texture_size*2, texture_slot=0, color=True, depth=True, grayscale=self.grayscale),
                     'antialias': ugl.create_fbo(gl.GL_TEXTURE_2D, aa_texture_size, aa_texture_size, texture_slot=0, color=True, depth=True, grayscale=self.grayscale)
                     }
