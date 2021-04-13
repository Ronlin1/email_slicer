def email_slicer():
    """
    A simple mail slicer that returns mail info to the user after input
    :return: --> info about mail --> String
    """

    # email = 'ronnie.atuhaire@octachart.com'
    # t_l_d_s = ['com', 'net', 'co.ug', 'us', 'tech', 'info', 'biz', '']
    email = input('Enter your full email address: ')

    # Getting names
    username = email[:email.index('@')]
    f_name, l_name = username.split('.')

    # Getting domain
    domain = email[email.index('@') + 1:]
    d_name, t_l_d = domain.split('.')
    display = f'You first name is {f_name.capitalize()} and last {l_name.capitalize()}, ' \
              f'registered on {d_name.capitalize()}\'s domain with ."{t_l_d.upper()}" as the TLD!'
    # print(type(f_name))
    return display


print(email_slicer())
