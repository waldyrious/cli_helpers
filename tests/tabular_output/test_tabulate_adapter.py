# -*- coding: utf-8 -*-
"""Test the tabulate output adapter."""

from __future__ import unicode_literals
from textwrap import dedent

import pytest

from cli_helpers.compat import HAS_PYGMENTS
from cli_helpers.tabular_output import tabulate_adapter

if HAS_PYGMENTS:
    from pygments.style import Style
    from pygments.token import Token


def test_tabulate_wrapper():
    """Test the *output_formatter.tabulate_wrapper()* function."""

    headers = ['letters', 'number']
    data = [['abc', 1], ['d', 456]]

    print("\n===> ascii: expected output")
    expected_output = dedent('''\
        +---------+--------+
        | letters | number |
        +---------+--------+
        | abc     | 1      |
        | d       | 456    |
        +---------+--------+''')
    print(expected_output)
    print("\n===> ascii: actual output")
    actual_output = "\n".join(tabulate_adapter.adapter(iter(data), headers, table_format='ascii'))
    print(actual_output)
    assert actual_output == expected_output

    # print("\n===> double: expected output")
    # expected_output = dedent('''\
    #     ╔═════════╦════════╗
    #     ║ letters ║ number ║
    #     ╠═════════╬════════╣
    #     ║ abc     ║      1 ║
    #     ║ d       ║    456 ║
    #     ╚═════════╩════════╝''')
    # print(expected_output)
    # print("\n===> double: actual output")
    # actual_output = "\n".join(tabulate_adapter.adapter(iter(data), headers, table_format='double'))
    # print(actual_output)
    # assert actual_output == expected_output

    # print("\n===> fancy_grid: expected output")
    # expected_output = dedent('''\
    #     ╒═════════╤════════╕
    #     │ letters │ number │
    #     ╞═════════╪════════╡
    #     │ abc     │      1 │
    #     ├─────────┼────────┤
    #     │ d       │    456 │
    #     ╘═════════╧════════╛''')
    # print(expected_output)
    # print("\n===> fancy_grid: actual output")
    # actual_output = "\n".join(tabulate_adapter.adapter(iter(data), headers, table_format='fancy_grid'))
    # print(actual_output)
    # assert actual_output == expected_output

    # print("\n===> github: expected output")
    # expected_output = dedent('''\
    #     | letters | number |
    #     |---------|--------|
    #     | abc     |      1 |
    #     | d       |    456 |''')
    # print(expected_output)
    # print("\n===> github: actual output")
    # actual_output = "\n".join(tabulate_adapter.adapter(iter(data), headers, table_format='github'))
    # print(actual_output)
    # assert actual_output == expected_output

    # print("\n===> ____: expected output")
    # expected_output = dedent('''\
    #     +---------+--------+
    #     | letters | number |
    #     +=========+========+
    #     | abc     |      1 |
    #     +---------+--------+
    #     | d       |    456 |
    #     +---------+--------+''')
    # print(expected_output)
    # print("\n===> github: actual output")
    # actual_output = "\n".join(tabulate_adapter.adapter(iter(data), headers, table_format='grid'))
    # assert actual_output == expected_output


    # print("\n===> ____: expected output")
    # expected_output = dedent('''\
    #     +---------+--------+
    #     | letters | number |
    #     +=========+========+
    #     | abc     |      1 |
    #     +---------+--------+
    #     | d       |    456 |
    #     +---------+--------+''')
    # print(expected_output)
    # print("\n===> github: actual output")
    # actual_output = "\n".join(tabulate_adapter.adapter(iter(data), headers, table_format='html'))
    # assert actual_output == expected_output



    # print("\n===> ____: expected output")
    # expected_output = dedent('''\
    #     letters  number
    #     -------  ------
    #     abc           1
    #     d           456''')
    # print(expected_output)
    # print("\n===> _____: actual output")
    # # TODO actually matches the simple format???
    # actual_output = "\n".join(tabulate_adapter.adapter(iter(data), headers, table_format='jira'))
    # assert actual_output == expected_output


    # print("\n===> ____: expected output")
    # expected_output = dedent('''\
    #     || letters || number ||
    #     | abc | 1 |
    #     | d | 456 |''')
    # print(expected_output)
    # print("\n===> _____: actual output")
    # actual_output = "\n".join(tabulate_adapter.adapter(iter(data), headers, table_format='jira'))
    # assert actual_output == expected_output


    # print("\n===> ____: expected output")
    # expected_output =
    # actual_output = "\n".join(tabulate_adapter.adapter(iter(data), headers, table_format='latex'))
    # assert actual_output == expected_output
    # dedent('''\
    #     letters	number
    #     abc    	     1
    #     d      	   456''')
    # print(expected_output)
    # print("\n===> _____: actual output")

    # print("\n===> ____: expected output")
    # expected_output =
    # actual_output = "\n".join(tabulate_adapter.adapter(iter(data), headers, table_format='latex_booktabs'))
    # assert actual_output == expected_output
    # dedent('''\
    #     letters	number
    #     abc    	     1
    #     d      	   456''')
    # print(expected_output)
    # print("\n===> _____: actual output")

    # print("\n===> ____: expected output")
    # expected_output =
    # actual_output = "\n".join(tabulate_adapter.adapter(iter(data), headers, table_format='mediawiki'))
    # assert actual_output == expected_output
    # dedent('''\
    #     |_.  letters |_. number |
    #     | abc  | 1 |
    #     | d  | 456 |''')
    # print(expected_output)
    # print("\n===> _____: actual output")

    # print("\n===> ____: expected output")
    # expected_output = dedent('''\
    #     || \'\'\' letters \'\'\' || \'\'\' number \'\'\' ||
    #     ||  abc  ||  1  ||
    #     ||  d  ||  456  ||''')
    # print(expected_output)
    # print("\n===> _____: actual output")
    # actual_output = "\n".join(tabulate_adapter.adapter(iter(data), headers, table_format='moinmoin'))
    # assert actual_output == expected_output

    # print("\n===> ____: expected output")
    # expected_output = dedent('''\
    #     | letters | number |
    #     |---------+--------|
    #     | abc     |      1 |
    #     | d       |    456 |''')
    # print(expected_output)
    # print("\n===> _____: actual output")
    # actual_output = "\n".join(tabulate_adapter.adapter(iter(data), headers, table_format='orgtbl'))
    # assert actual_output == expected_output


    # print("\n===> ____: expected output")
    # expected_output = dedent('''\
    #     | letters | number |
    #     |:--------|-------:|
    #     | abc     |      1 |
    #     | d       |    456 |''')
    # print(expected_output)
    # print("\n===> _____: actual output")
    # actual_output = "\n".join(tabulate_adapter.adapter(iter(data), headers, table_format='pipe'))
    # assert actual_output == expected_output


    # print("\n===> ____: expected output")
    # expected_output = dedent('''\
    #     letters  number
    #     abc           1
    #     d           456''')
    # print(expected_output)
    # print("\n===> _____: actual output")
    # actual_output = "\n".join(tabulate_adapter.adapter(iter(data), headers, table_format='plain'))
    # assert actual_output == expected_output


    # print("\n===> ____: expected output")
    # expected_output = dedent('''\
    #     +---------+--------+
    #     | letters | number |
    #     |---------+--------|
    #     | abc     |      1 |
    #     | d       |    456 |
    #     +---------+--------+''')
    # print(expected_output)
    # print("\n===> _____: actual output")
    # actual_output = "\n".join(tabulate_adapter.adapter(iter(data), headers, table_format='psql'))
    # assert actual_output == expected_output


    # print("\n===> ____: expected output")
    # expected_output = dedent('''\
    #     ┌─────────┬────────┐
    #     │ letters │ number │
    #     ├─────────┼────────┤
    #     │ abc     │      1 │
    #     │ d       │    456 │
    #     └─────────┴────────┘''')
    # print(expected_output)
    # print("\n===> _____: actual output")
    # actual_output = "\n".join(tabulate_adapter.adapter(iter(data), headers, table_format='psql_unicode'))
    # assert actual_output == expected_output


    # print("\n===> ____: expected output")
    # expected_output = dedent('''\
    #     =======  ======
    #     letters  number
    #     =======  ======
    #     abc           1
    #     d           456
    #     =======  ======''')
    # print(expected_output)
    # print("\n===> _____: actual output")
    # actual_output = "\n".join(tabulate_adapter.adapter(iter(data), headers, table_format='rst'))
    # assert actual_output == expected_output


    # print("\n===> ____: expected output")
    # expected_output = dedent('''\
    #     letters  number
    #     -------  ------
    #     abc           1
    #     d           456''')
    # print(expected_output)
    # print("\n===> _____: actual output")
    # actual_output = "\n".join(tabulate_adapter.adapter(iter(data), headers, table_format='simple'))
    # assert actual_output == expected_output


    # print("\n===> ____: expected output")
    # expected_output = dedent('''\
    #     |_.  letters |_. number |
    #     | abc  | 1 |
    #     | d  | 456 |''')
    # print(expected_output)
    # print("\n===> _____: actual output")
    # actual_output = "\n".join(tabulate_adapter.adapter(iter(data), headers, table_format='textile'))
    # assert actual_output == expected_output


    data = [['{1,2,3}', '{{1,2},{3,4}}', '{å,魚,текст}'], ['{}', '<null>', '{<null>}']]
    headers = ['bigint_array', 'nested_numeric_array', '配列']
    actual_output = "\n".join(tabulate_adapter.adapter(iter(data), headers, table_format='psql'))
    assert actual_output == expected_output
    expected_output = dedent('''\
        +--------------+----------------------+--------------+
        | bigint_array | nested_numeric_array | 配列         |
        |--------------+----------------------+--------------|
        | {1,2,3}      | {{1,2},{3,4}}        | {å,魚,текст} |
        | {}           | <null>               | {<null>}     |
        +--------------+----------------------+--------------+''')


def test_markup_format():
    """Test that markup formats do not have number align or string align."""
    data = [['abc', 1], ['d', 456]]
    headers = ['letters', 'number']
    output = tabulate_adapter.adapter(iter(data), headers, table_format='mediawiki')
    assert "\n".join(output) == dedent('''\
        {| class="wikitable" style="text-align: left;"
        |+ <!-- caption -->
        |-
        ! letters !! number
        |-
        | abc || 1
        |-
        | d || 456
        |}''')


@pytest.mark.skipif(not HAS_PYGMENTS, reason='requires the Pygments library')
def test_style_output_table():
    """Test that *style_output_table()* styles the output table."""

    class CliStyle(Style):
        default_style = ""
        styles = {
            Token.Output.TableSeparator: 'ansibrightred',
        }
    headers = ['h1', 'h2']
    data = [['观音', '2'], ['Ποσειδῶν', 'b']]
    style_output_table = tabulate_adapter.style_output_table('psql')

    style_output_table(data, headers, style=CliStyle)
    output = tabulate_adapter.adapter(iter(data), headers, table_format='psql')
    PLUS = '\x1b[91m+\x1b[39m'
    MINUS = '\x1b[91m-\x1b[39m'
    PIPE = '\x1b[91m|\x1b[39m'

    expected = dedent('''\
        +----------+----+
        | h1       | h2 |
        |----------+----|
        | 观音     | 2  |
        | Ποσειδῶν | b  |
        +----------+----+'''
    ).replace('+', PLUS).replace('-', MINUS).replace('|', PIPE)

    assert "\n".join(output) == expected
