# PyApply


PyApply is a command-line interface (CLI) tool designed to automate coverletter creation, significantly reducing the time required to perform them.
Heres a  Walkthrough on Medium and Youtube
  
> [!NOTE]
> Currently, this app only works for ASU Student jobs.

## Features

- **Cover Letter Generation**: PyApply can generate cover letters based on provided job descriptions and user details.

- **Preset and Custom Themes**: Choose from predefined themes or use your own custom theme for the cover letters.

- **User Profile Management**: Set user details globally or for specific tasks using JSON files.
## Installation

  

```bash

pip install pyapply

```

  

## Usage

>[!NOTE]
>if the below commands dont work directly, try adding ```python -m ``` before every command listed below.
> Example: ```python -m pyapply about```

### About
```bash
pyapply about
```


### Profile Setup

#### To set User Profile
```bash
pyapply set_user <path/to/save/asujobs>
```

#### To set context information for coverletters
```bash

pyapply set_resume <path/of/resume.txt>
```

## Generate cover letters

```bash
pyapply listen
```

Coverletters will be generated automatically as soon as the clipboard values change.

  

## Performance

PyApply can convert a process that typically takes 5-10 minutes into a task that takes just 30 seconds.

  

<!-- ## Contributing

Contributions are welcome! Please read the contributing guidelines before getting started. -->


  

License [MIT](https://choosealicense.com/licenses/mit/)
