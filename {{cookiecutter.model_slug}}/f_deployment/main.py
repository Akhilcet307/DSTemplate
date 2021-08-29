from {{cookiecutter.model_slug}} import {{cookiecutter.model_class}}

import click


###
### Leverage click to create command line parameters to control how model would work
### in a batch-mode for a production environment
@click.command()
@click.option('--example', default=1, help='Example help')
def main(example):
    
    ###
    ### Instantiate model class 
    model = {{cookiecutter.model_class}}()
    
    
    ###
    ### Load and prepare data


    ###
    ### 
    model.predict({"example":example})
    
if __name__ == "__main__":
    main()