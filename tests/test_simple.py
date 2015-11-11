import negotiator as ng


def test_simple_example():
    default_params = ng.AcceptParameters(
        ng.ContentType("text/html"), ng.Language("en")
    )

    acceptable = [
        ng.AcceptParameters(ng.ContentType("text/html"), ng.Language("en")),
        ng.AcceptParameters(ng.ContentType("text/json"), ng.Language("en")),
    ]

    cn = ng.ContentNegotiator(default_params, acceptable)
    result = cn.negotiate(accept='text/json;q=1.0, text/html;q=0.9')

    assert result.language == ng.Language('en')
    assert result.content_type == ng.ContentType('text/json')


def test_webp_default_png():
    default_params = ng.AcceptParameters(ng.ContentType("image/png"))

    acceptable = [
        default_params,
        ng.AcceptParameters(ng.ContentType("image/webp")),
    ]

    cn = ng.ContentNegotiator(default_params, acceptable)
    result = cn.negotiate(accept=(
        'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,'
        '*/*;q=0.8'
    ))

    assert result.content_type == ng.ContentType('image/webp')

    result = cn.negotiate(accept=(
        'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
    ))

    assert result.content_type == ng.ContentType('image/png')
