def initialize_user_details(path):
    template = open('template.txt', 'r').read()
    userdetails = open(path, 'r').read()
    prompt = template+userdetails+"""

    ##JOB Description##
    """
    open('coverletter.txt', 'w').write(prompt)
    
    
    