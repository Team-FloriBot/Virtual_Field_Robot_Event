#!/usr/bin/env python3

from field_2d_generator import Field2DGenerator
import rospkg
import argparse
import inspect
import os

if __name__ == "__main__":
    # get the possible arguments of the generator and default values
    argspec = inspect.getfullargspec(Field2DGenerator.__init__)
    possible_kwargs = argspec.args[1:]
    defaults = argspec.defaults
    
    # construct an ArgumentParser that takes these arguments
    parser = argparse.ArgumentParser(description='Generate a virtual maize field world for gazebo')
    for argname, default in zip(possible_kwargs, defaults):
        # we analyze the default value's type to guess the type for that argument
        parser.add_argument("--"+argname, type=type(default), help='default_value: {}'.format(default), required=False)
    
    # get a dict representation of the arguments and call our constructor with them as kwargs
    args = vars(parser.parse_args())
    args = {k:v for k,v in args.items() if v is not None}
    pk = Field2DGenerator(**args)
    
    # generate the template and write it to a file
    pkg_path = rospkg.RosPack().get_path('virtual_maize_field')
    template_path = os.path.join(pkg_path, "scripts/field.world.template")
    template = open(template_path).read()
    generated_sdf = pk.render_to_template(template)
    out_path = os.path.join(pkg_path, "worlds/generated.world")
    with open(out_path, "w") as f:
        f.write(generated_sdf)
    