print("hello proloy")
import magpylib as magpy
cube1 = magpy.magnet.Cuboid(
    magnetization=(0,0,1),
    dimension=(1,1,1),
)
cube2 = magpy.magnet.Cuboid(
    magnetization=(0,0,1),
    dimension=(2,2,2),
    position(2,0,0)
)
magpy.show(cube1,cube2)