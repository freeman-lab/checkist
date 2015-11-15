def opts(opt, valid):
    if not opt in valid:
        raise ValueError("Option must be one of %s, got '%s'" % (str(valid)[1:-1], opt))