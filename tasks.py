from invoke import task

@task
def lint(ctx):
    # currently just a light weight commandline call to deal with preferred conventions
    # could look at options to use md configuration file or other extensible solution
    # along with a method for checking for dead links
    ctx.run("mdl -r ~MD009,~MD013,~MD036,~MD029,~MD001,~MD024,~MD026,~MD025,~MD033 .")






import json as js
import os
from jinja2 import Environment, FileSystemLoader
import argparse

parser = argparse.ArgumentParser(description='generate kops config template')
parser.add_argument('customer_list', type=str, nargs='?', help='filename of customer and namespace list')

args = parser.parse_args()
customer_list = args.customer_list

PATH = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_ENVIRONMENT = Environment(
    autoescape=False,
    loader=FileSystemLoader(os.path.join(PATH)),
    trim_blocks=False)

DICTIONARY = {}

def renderRBAC():

    # example
    DICTIONARY['nodes'] = nodes
    template = TEMPLATE_ENVIRONMENT.get_template("template.yml")
    renderedtemplate = template.render(**DICTIONARY)

    f = open("{}_cluster.yml".format(vpc_env), 'w')
    f.write(renderedtemplate)  # python will convert \n to os.linesep
    f.close()
