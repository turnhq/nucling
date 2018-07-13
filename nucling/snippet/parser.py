import re


regex_numbers = re.compile( '[0-9]+' )


fix_values_of_bool = {
    'true': True,
    'false': False,
    '0': False,
}


def to_bool( value ):
    """
    transform the value in a bool using a fixed list of values

    Arguments
    ---------
    value: any

    Returns
    -------
    bool

    Examples
    >>>to_bool( '0' )
    False
    >>>to_bool( 'false' )
    False
    >>>to_bool( '1' )
    True
    >>>to_bool( 'true' )
    True
    >>>to_bool( object() )
    True
    """
    if isinstance( value, str ):
        return fix_values_of_bool.get( value.lower(), bool( value ) )
    return fix_values_of_bool.get( value, bool( value ) )


def clean_zipcode( zipcode ):
    """
    get a string with only the digits of the zipcode

    Parameters
    ----------
    zipcode: string

    Raises
    ------
    TypeError
        when the zipcode is not a type of string

    Returns
    -------
    string
        the zipcode with only the numbers
    None
        when the zipcode is None

    Examples
    --------
    >>>clean_zipcode( "12345" )
    "12345"
    >>>clean_zipcode( "12345-67890" )
    "1234567890"
    >>>clean_zipcode( "asdf" )
    ""
    >>>clean_zipcode( "asdf-12345" )
    "12345"
    >>>clean_zipcode( None )
    None
    """
    if zipcode is None:
        return zipcode
    if not isinstance( zipcode, str ):
        raise TypeError(
            "expected the zipcode are a '{}' type but receive a '{}'"
            .format( type( '' ), type( zipcode ) ) )
    results = regex_numbers.findall( zipcode )
    return "".join( results )
