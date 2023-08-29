# Manim Guides

To setup the development workspace run:

```bash
pipenv install
```

It is recommended to setup the manim VS code extension, and set the manim executable path to whatever output this command gives you:

```bash
pipenv run which manimce
```

This manim has custom plugins included, however might rise some issues.
To run stable and isolated manim interactively:

```bash
docker run --rm -it -w $PWD -v $PWD:$PWD --name dev-manim manimcommunity/manim /bin/bash
```

To keep runing for development

```sh
watchexec --watch ./*.py "docker run --rm -w $PWD -v $PWD:$PWD manimcommunity/manim manim scene.py GoChannels"
```