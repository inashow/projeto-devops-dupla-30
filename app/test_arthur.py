from app import app


def test_saude_informa_versao_em_json():
    resposta = app.test_client().get("/saude")
    assert resposta.status_code == 200
    assert resposta.is_json
    dados = resposta.get_json()
    assert "versao" in dados
    assert isinstance(dados["versao"], str)
    assert dados["versao"].strip()
