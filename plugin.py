"""
This is a working sample Generated Parameter Options CloudBolt plug-in for you to start with.
The get_options_list method is required, but you can change all the code within it.
See the "Generated Parameter Options" section of the docs for more info and the CloudBolt forge
for more examples: https://github.com/CloudBoltSoftware/cloudbolt-forge/tree/master/actions/cloudbolt_plugins
"""
from infrastructure.models import Environment


def get_options_list(field, group=None, control_value=None, **kwargs):
    """
    A plug-in that returns options for tree species.

    :param field: The field you are generating options for.
    """
    # # Define the database value and display value for each option as a list of tuples.

    options = [ ]

    if control_value:
        env = Environment.objects.get(id=control_value)
        options = [(s.id, s.name) for s in env.networks()]

    return {
        'options': options,
    }
