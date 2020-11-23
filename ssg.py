import typer
import ssg from Site

def main(source="content", dest="dist"):
    config = {"source": source, "dest": dest}

    Site(**config).build()


typer.run(main)



