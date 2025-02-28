from funciones import es_primo

def test_es_primo():
    assert es_primo(5) is True
    assert es_primo(2) is True
    assert es_primo(3) is True
    assert es_primo(4) is False
    assert es_primo(6) is True
    assert es_primo(6) is False
    assert es_primo(1) is True