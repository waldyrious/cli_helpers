# -*- coding: utf-8 -*-
"""Test the generic output formatter interface."""

from __future__ import unicode_literals
from decimal import Decimal
from textwrap import dedent

import pytest

from cli_helpers.tabular_output import format_output, TabularOutputFormatter
from cli_helpers.compat import binary_type, text_type
from cli_helpers.utils import strip_ansi


def test_tabular_output_formatter():
    """Test the TabularOutputFormatter class."""
    headers = ['numeric', 'text1', 'text2']
    data = [
        [Decimal(1), "abc", "Lorem"],
        [Decimal("11.1"), "defg", "Ipsum"],
        [Decimal("1.1"), "hi", None],
        [0, "Pablo\rß\n", "Foobar"],
        [1234.567, "John", '"Johnny" Smith'],
    ]


    expected = dedent("""\
        +---------+------------+----------------+
        | numeric | text1      | text2          |
        +---------+------------+----------------+
        | 1       | abc        | Lorem          |
        | 11.1    | defg       | Ipsum          |
        | 1.1     | hi         | <null>         |
        | 0       | Pablo\\rß\\n | Foobar         |
        | 1234.57 | John       | "Johnny" Smith |
        +---------+------------+----------------+"""
    )
    print("\n==== ascii: expected ====")
    print(expected)
    print("\n==== ascii: actual ====")
    print("\n".join(TabularOutputFormatter().format_output(
        iter(data), headers, format_name='ascii')))
    assert expected == "\n".join(TabularOutputFormatter().format_output(
        iter(data), headers, format_name='ascii'))


    expected = dedent("""\
        numeric,text1,text2
        1,abc,Lorem
        11.1,defg,Ipsum
        1.1,hi,
        0,Pablo\\rß\\n,Foobar
        1234.567,John,\"""Johnny"" Smith\""""
    )
    print("\n==== csv: expected ====")
    print(expected)
    print("\n==== csv: actual ====")
    print("\n".join(TabularOutputFormatter().format_output(
        iter(data), headers, format_name='csv')))
    assert expected == "\n".join(TabularOutputFormatter().format_output(
        iter(data), headers, format_name='csv'))


    expected = dedent("""\
        numeric	text1	text2
        1	abc	Lorem
        11.1	defg	Ipsum
        1.1	hi\t
        0	Pablo\\rß\\n	Foobar
        1234.567	John	\"""Johnny"" Smith\""""
    )
    print("\n==== csv-tab: expected ====")
    print(expected)
    print("\n==== csv-tab: actual ====")
    print("\n".join(TabularOutputFormatter().format_output(
        iter(data), headers, format_name='csv-tab')))
    assert expected == "\n".join(TabularOutputFormatter().format_output(
        iter(data), headers, format_name='csv-tab'))


    expected = dedent("""\
        ╔═════════╦════════════╦════════════════╗
        ║ numeric ║ text1      ║ text2          ║
        ╠═════════╬════════════╬════════════════╣
        ║    1    ║ abc        ║ Lorem          ║
        ║   11.1  ║ defg       ║ Ipsum          ║
        ║    1.1  ║ hi         ║ <null>         ║
        ║    0    ║ Pablo\\rß\\n ║ Foobar         ║
        ║ 1234.57 ║ John       ║ "Johnny" Smith ║
        ╚═════════╩════════════╩════════════════╝"""
    )
    print("\n==== double: expected ====")
    print(expected)
    print("\n==== double: actual ====")
    print("\n".join(TabularOutputFormatter().format_output(
        iter(data), headers, format_name='double')))
    assert expected == "\n".join(TabularOutputFormatter().format_output(
        iter(data), headers, format_name='double'))


    expected = dedent("""\
        ╒═════════╤═══════╤════════════════╕
        │ numeric │ text1 │ text2          │
        ╞═════════╪═══════╪════════════════╡
        │    1    │ abc   │ Lorem          │
        ├─────────┼───────┼────────────────┤
        │   11.1  │ defg  │ Ipsum          │
        ├─────────┼───────┼────────────────┤
        │    1.1  │ hi    │ <null>         │
        ├─────────┼───────┼────────────────┤
        │    0    │ Pablo │ Foobar         │
        │         │ ß     │                │
        ├─────────┼───────┼────────────────┤
        │ 1234.57 │ John  │ "Johnny" Smith │
        ╘═════════╧═══════╧════════════════╛"""
    )
    print("\n==== fancy_grid: expected ====")
    print(expected)
    print("\n==== fancy_grid: actual ====")
    print("\n".join(TabularOutputFormatter().format_output(
        iter(data), headers, format_name='fancy_grid')))
    assert expected == "\n".join(TabularOutputFormatter().format_output(
        iter(data), headers, format_name='fancy_grid'))


    expected = dedent("""\
        | numeric | text1      | text2          |
        |---------|------------|----------------|
        |    1    | abc        | Lorem          |
        |   11.1  | defg       | Ipsum          |
        |    1.1  | hi         | <null>         |
        |    0    | Pablo\\rß\\n | Foobar         |
        | 1234.57 | John       | "Johnny" Smith |"""
    )
    print("\n==== github: expected ====")
    print(expected)
    print("\n==== github: actual ====")
    print("\n".join(TabularOutputFormatter().format_output(
        iter(data), headers, format_name='github')))
    assert expected == "\n".join(TabularOutputFormatter().format_output(
        iter(data), headers, format_name='github'))


    expected = dedent("""\
        +---------+-------+----------------+
        | numeric | text1 | text2          |
        +=========+=======+================+
        |    1    | abc   | Lorem          |
        +---------+-------+----------------+
        |   11.1  | defg  | Ipsum          |
        +---------+-------+----------------+
        |    1.1  | hi    | <null>         |
        +---------+-------+----------------+
        |    0    | Pablo | Foobar         |
        |         | ß     |                |
        +---------+-------+----------------+
        | 1234.57 | John  | "Johnny" Smith |
        +---------+-------+----------------+"""
    )
    print("\n==== grid: expected ====")
    print(expected)
    print("\n==== grid: actual ====")
    print("\n".join(TabularOutputFormatter().format_output(
        iter(data), headers, format_name='grid')))
    assert expected == "\n".join(TabularOutputFormatter().format_output(
        iter(data), headers, format_name='grid'))


    expected = dedent("""\
        <table>
        <thead>
        <tr><th>numeric</th><th>text1</th><th>text2</th></tr>
        </thead>
        <tbody>
        <tr><td>1</td><td>abc</td><td>Lorem</td></tr>
        <tr><td>11.1</td><td>defg</td><td>Ipsum</td></tr>
        <tr><td>1.1</td><td>hi</td><td>&lt;null&gt;</td></tr>
        <tr><td>0</td><td>Pablo\\rß\\n</td><td>Foobar</td></tr>
        <tr><td>1234.57</td><td>John</td><td>&quot;Johnny&quot; Smith</td></tr>
        </tbody>
        </table>"""
    )
    print("\n==== html: expected ====")
    print(expected)
    print("\n==== html: actual ====")
    print("\n".join(TabularOutputFormatter().format_output(
        iter(data), headers, format_name='html')))
    assert expected == "\n".join(TabularOutputFormatter().format_output(
        iter(data), headers, format_name='html'))


    expected = dedent("""\
        || numeric || text1 || text2 ||
        | 1 | abc | Lorem |
        | 11.1 | defg | Ipsum |
        | 1.1 | hi | <null> |
        | 0 | Pablo\\rß\\n | Foobar |
        | 1234.57 | John | "Johnny" Smith |"""
    )
    print("\n==== jira: expected ====")
    print(expected)
    print("\n==== jira: actual ====")
    print("\n".join(TabularOutputFormatter().format_output(
        iter(data), headers, format_name='jira')))
    assert expected == "\n".join(TabularOutputFormatter().format_output(
        iter(data), headers, format_name='jira'))


    expected = dedent("""\
        \\begin{tabular}{lll}
        \\hline
         numeric & text1 & text2 \\\\
        \\hline
         1 & abc & Lorem \\\\
         11.1 & defg & Ipsum \\\\
         1.1 & hi & \\ensuremath{<}null\\ensuremath{>} \\\\
         0 & Pablo\\textbackslash{}rß\\textbackslash{}n & Foobar \\\\
         1234.57 & John & "Johnny" Smith \\\\
        \\hline
        \\end{tabular}"""
    )
    print("\n==== latex: expected ====")
    print(expected)
    print("\n==== latex: actual ====")
    print("\n".join(TabularOutputFormatter().format_output(
        iter(data), headers, format_name='latex')))
    assert expected == "\n".join(TabularOutputFormatter().format_output(
        iter(data), headers, format_name='latex'))


    expected = dedent("""\
        \\begin{tabular}{lll}
        \\toprule
         numeric & text1 & text2 \\\\
        \\midrule
         1 & abc & Lorem \\\\
         11.1 & defg & Ipsum \\\\
         1.1 & hi & \\ensuremath{<}null\\ensuremath{>} \\\\
         0 & Pablo\\textbackslash{}rß\\textbackslash{}n & Foobar \\\\
         1234.57 & John & "Johnny" Smith \\\\
        \\bottomrule
        \\end{tabular}"""
    )
    print("\n==== latex_booktabs: expected ====")
    print(expected)
    print("\n==== latex_booktabs: actual ====")
    print("\n".join(TabularOutputFormatter().format_output(
        iter(data), headers, format_name='latex_booktabs')))
    assert expected == "\n".join(TabularOutputFormatter().format_output(
        iter(data), headers, format_name='latex_booktabs'))


    expected = dedent("""\
        {| class="wikitable" style="text-align: left;"
        |+ <!-- caption -->
        |-
        ! numeric !! text1 !! text2
        |-
        | 1 || abc || Lorem
        |-
        | 11.1 || defg || Ipsum
        |-
        | 1.1 || hi || <null>
        |-
        | 0 || Pablo\\rß\\n || Foobar
        |-
        | 1234.57 || John || "Johnny" Smith
        |}"""
    )
    print("\n==== mediawiki: expected ====")
    print(expected)
    print("\n==== mediawiki: actual ====")
    print("\n".join(TabularOutputFormatter().format_output(
        iter(data), headers, format_name='mediawiki')))
    assert expected == "\n".join(TabularOutputFormatter().format_output(
        iter(data), headers, format_name='mediawiki'))


    expected = dedent("""\
        || ''' numeric ''' || ''' text1 ''' || ''' text2 ''' ||
        ||  1  ||  abc  ||  Lorem  ||
        ||  11.1  ||  defg  ||  Ipsum  ||
        ||  1.1  ||  hi  ||  <null>  ||
        ||  0  ||  Pablo\\rß\\n  ||  Foobar  ||
        ||  1234.57  ||  John  ||  "Johnny" Smith  ||"""
    )
    print("\n==== moinmoin: expected ====")
    print(expected)
    print("\n==== moinmoin: actual ====")
    print("\n".join(TabularOutputFormatter().format_output(
        iter(data), headers, format_name='moinmoin')))
    assert expected == "\n".join(TabularOutputFormatter().format_output(
        iter(data), headers, format_name='moinmoin'))


    expected = dedent("""\
        | numeric | text1      | text2          |
        |---------+------------+----------------|
        |    1    | abc        | Lorem          |
        |   11.1  | defg       | Ipsum          |
        |    1.1  | hi         | <null>         |
        |    0    | Pablo\\rß\\n | Foobar         |
        | 1234.57 | John       | "Johnny" Smith |"""
    )
    print("\n==== orgtbl: expected ====")
    print(expected)
    print("\n==== orgtbl: actual ====")
    print("\n".join(TabularOutputFormatter().format_output(
        iter(data), headers, format_name='orgtbl')))
    assert expected == "\n".join(TabularOutputFormatter().format_output(
        iter(data), headers, format_name='orgtbl'))


    expected = dedent("""\
        | numeric | text1      | text2          |
        |--------:|:-----------|:---------------|
        |    1    | abc        | Lorem          |
        |   11.1  | defg       | Ipsum          |
        |    1.1  | hi         | <null>         |
        |    0    | Pablo\\rß\\n | Foobar         |
        | 1234.57 | John       | "Johnny" Smith |"""
    )
    print("\n==== pipe: expected ====")
    print(expected)
    print("\n==== pipe: actual ====")
    print("\n".join(TabularOutputFormatter().format_output(
        iter(data), headers, format_name='pipe')))
    assert expected == "\n".join(TabularOutputFormatter().format_output(
        iter(data), headers, format_name='pipe'))


    expected = dedent("""\
        numeric  text1       text2
           1     abc         Lorem
          11.1   defg        Ipsum
           1.1   hi          <null>
           0     Pablo\\rß\\n  Foobar
        1234.57  John        "Johnny" Smith"""
    )
    print("\n==== plain: expected ====")
    print(expected)
    print("\n==== plain: actual ====")
    print("\n".join(TabularOutputFormatter().format_output(
        iter(data), headers, format_name='plain')))
    assert expected == "\n".join(TabularOutputFormatter().format_output(
        iter(data), headers, format_name='plain'))


    expected = dedent("""\
        +---------+------------+----------------+
        | numeric | text1      | text2          |
        |---------+------------+----------------|
        |    1    | abc        | Lorem          |
        |   11.1  | defg       | Ipsum          |
        |    1.1  | hi         | <null>         |
        |    0    | Pablo\\rß\\n | Foobar         |
        | 1234.57 | John       | "Johnny" Smith |
        +---------+------------+----------------+"""
    )
    print("\n==== psql: expected ====")
    print(expected)
    print("\n==== psql: actual ====")
    print("\n".join(TabularOutputFormatter().format_output(
        iter(data), headers, format_name='psql')))
    assert expected == "\n".join(TabularOutputFormatter().format_output(
        iter(data), headers, format_name='psql'))


    expected = dedent("""\
        ┌─────────┬────────────┬────────────────┐
        │ numeric │ text1      │ text2          │
        ├─────────┼────────────┼────────────────┤
        │    1    │ abc        │ Lorem          │
        │   11.1  │ defg       │ Ipsum          │
        │    1.1  │ hi         │ <null>         │
        │    0    │ Pablo\\rß\\n │ Foobar         │
        │ 1234.57 │ John       │ "Johnny" Smith │
        └─────────┴────────────┴────────────────┘"""
    )
    print("\n==== psql_unicode: expected ====")
    print(expected)
    print("\n==== psql_unicode: actual ====")
    print("\n".join(TabularOutputFormatter().format_output(
        iter(data), headers, format_name='psql_unicode')))
    assert expected == "\n".join(TabularOutputFormatter().format_output(
        iter(data), headers, format_name='psql_unicode'))


    expected = dedent("""\
        =======  ==========  ==============
        numeric  text1       text2
        =======  ==========  ==============
           1     abc         Lorem
          11.1   defg        Ipsum
           1.1   hi          <null>
           0     Pablo\\rß\\n  Foobar
        1234.57  John        "Johnny" Smith
        =======  ==========  =============="""
    )
    print("\n==== rst: expected ====")
    print(expected)
    print("\n==== rst: actual ====")
    print("\n".join(TabularOutputFormatter().format_output(
        iter(data), headers, format_name='rst')))
    assert expected == "\n".join(TabularOutputFormatter().format_output(
        iter(data), headers, format_name='rst'))


    expected = dedent("""\
        numeric  text1       text2
        -------  ----------  --------------
           1     abc         Lorem
          11.1   defg        Ipsum
           1.1   hi          <null>
           0     Pablo\\rß\\n  Foobar
        1234.57  John        "Johnny" Smith"""
    )
    print("\n==== simple: expected ====")
    print(expected)
    print("\n==== simple: actual ====")
    print("\n".join(TabularOutputFormatter().format_output(
        iter(data), headers, format_name='simple')))
    assert expected == "\n".join(TabularOutputFormatter().format_output(
        iter(data), headers, format_name='simple'))


    expected = dedent("""\
        |_.  numeric |_. text1 |_. text2 |
        | 1  | abc | Lorem |
        | 11.1  | defg | Ipsum |
        | 1.1  | hi | <null> |
        | 0  | Pablo\\rß\\n | Foobar |
        | 1234.57  | John | "Johnny" Smith |"""
    )
    print("\n==== textile: expected ====")
    print(expected)
    print("\n==== textile: actual ====")
    print("\n".join(TabularOutputFormatter().format_output(
        iter(data), headers, format_name='textile')))
    assert expected == "\n".join(TabularOutputFormatter().format_output(
        iter(data), headers, format_name='textile'))


    expected = dedent("""\
        numeric	text1	text2
        1	abc	Lorem
        11.1	defg	Ipsum
        1.1	hi\t
        0	Pablo\\rß\\n	Foobar
        1234.567	John	"Johnny" Smith"""
    )
    print("\n==== tsv: expected ====")
    print(expected)
    print("\n==== tsv: actual ====")
    print("\n".join(TabularOutputFormatter().format_output(
        iter(data), headers, format_name='tsv')))
    assert expected == "\n".join(TabularOutputFormatter().format_output(
        iter(data), headers, format_name='tsv'))


    expected = dedent("""\
        ***************************[ 1. row ]***************************
        numeric | 1
        text1   | abc
        text2   | Lorem
        ***************************[ 2. row ]***************************
        numeric | 11.1
        text1   | defg
        text2   | Ipsum
        ***************************[ 3. row ]***************************
        numeric | 1.1
        text1   | hi
        text2   | <null>
        ***************************[ 4. row ]***************************
        numeric | 0
        text1   | Pablo\rß\n
        text2   | Foobar
        ***************************[ 5. row ]***************************
        numeric | 1234.567
        text1   | John
        text2   | "Johnny" Smith"""
    )
    print("\n==== vertical: expected ====")
    print(expected)
    print("\n==== vertical: actual ====")
    print("\n".join(TabularOutputFormatter().format_output(
        iter(data), headers, format_name='vertical')))
    assert expected == "\n".join(TabularOutputFormatter().format_output(
        iter(data), headers, format_name='vertical'))


def test_tabular_format_output_wrapper():
    """Test the format_output() wrapper."""
    data = [['1', None], ['2', 'Sam'],
            ['3', 'Joe']]
    headers = ['id', 'name']
    expected = dedent('''\
        +----+------+
        | id | name |
        +----+------+
        | 1  | N/A  |
        | 2  | Sam  |
        | 3  | Joe  |
        +----+------+''')

    assert expected == "\n".join(format_output(iter(data), headers, format_name='ascii',
                                               missing_value='N/A'))


def test_additional_preprocessors():
    """Test that additional preprocessors are run."""
    def hello_world(data, headers, **_):
        # Sample preprocessor that changes the exact value "hello" to "hello, world"
        def hello_world_data(data):
            for row in data:
                for i, value in enumerate(row):
                    if value == 'hello':
                        row[i] = "{}, world".format(value)
                yield row
        return hello_world_data(data), headers

    data = [['foo', None], ['hello!', 'hello']]
    headers = 'ab'

    expected = dedent('''\
        +--------+--------------+
        | a      | b            |
        +--------+--------------+
        | foo    | hello        |
        | hello! | hello, world |
        +--------+--------------+''')

    assert expected == "\n".join(TabularOutputFormatter().format_output(
        iter(data), headers, format_name='ascii', preprocessors=(hello_world,),
        missing_value='hello'))


def test_format_name_attribute():
    """Test the the format_name attribute be set and retrieved."""
    formatter = TabularOutputFormatter(format_name='plain')
    assert formatter.format_name == 'plain'
    formatter.format_name = 'simple'
    assert formatter.format_name == 'simple'

    with pytest.raises(ValueError):
        formatter.format_name = 'foobar'


def test_unsupported_format():
    """Test that TabularOutputFormatter rejects unknown formats."""
    formatter = TabularOutputFormatter()

    with pytest.raises(ValueError):
        formatter.format_name = 'foobar'

    with pytest.raises(ValueError):
        formatter.format_output((), (), format_name='foobar')


def test_tabulate_ansi_escape_in_default_value():
    """Test that ANSI escape codes work with tabulate."""

    data = [['1', None], ['2', 'Sam'],
            ['3', 'Joe']]
    headers = ['id', 'name']

    styled = format_output(iter(data), headers, format_name='psql',
                           missing_value='\x1b[38;5;10mNULL\x1b[39m')
    unstyled = format_output(iter(data), headers, format_name='psql',
                             missing_value='NULL')

    stripped_styled = [strip_ansi(s) for s in styled]

    assert list(unstyled) == stripped_styled


def test_get_type():
    """Test that _get_type returns the expected type."""
    formatter = TabularOutputFormatter()

    tests = ((1, int), (2.0, float), (b'binary', binary_type),
             ('text', text_type), (None, type(None)), ((), text_type))

    for value, data_type in tests:
        assert data_type is formatter._get_type(value)


def test_provide_column_types():
    """Test that provided column types are passed to preprocessors."""
    expected_column_types = (bool, float)
    data = ((1, 1.0), (0, 2))
    headers = ('a', 'b')

    def preprocessor(data, headers, column_types=(), **_):
        assert expected_column_types == column_types
        return data, headers

    format_output(data, headers, 'csv',
                  column_types=expected_column_types,
                  preprocessors=(preprocessor,))


def test_enforce_iterable():
    """Test that all output formatters accept iterable"""
    formatter = TabularOutputFormatter()
    loremipsum = 'lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod'.split(' ')

    for format_name in formatter.supported_formats:
        formatter.format_name = format_name
        try:
            formatted = next(formatter.format_output(
                zip(loremipsum), ['lorem']))
        except TypeError:
            assert False, "{0} doesn't return iterable".format(format_name)


def test_all_text_type():
    """Test the TabularOutputFormatter class."""
    data = [[1, u"", None, Decimal(2)]]
    headers = ['col1', 'col2', 'col3', 'col4']
    output_formatter = TabularOutputFormatter()
    for format_name in output_formatter.supported_formats:
        for row in output_formatter.format_output(iter(data), headers, format_name=format_name):
            assert isinstance(row, text_type), "not unicode for {}".format(format_name)
