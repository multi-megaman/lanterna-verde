"""
Script to populate `Questões` in lanternaverde_web with the Greenwashing Accute
Score Questionnary.
"""
from lanternaverde_web.models import Questao

# pylint: disable=E1101
def run():
    """Flow of object creations for the populate script"""
    Questao.objects.create(
        dimension='D1',
        body="Does the claim suggest that the product or service is green "
        "based on a narrow set of attributes without attention to other "
        "environmental issues?")
    Questao.objects.create(
        dimension='D1',
        body="Cannot the claim be sustained by easily accessible supporting "
        "information or by reliable third-party certification?")
    Questao.objects.create(
        dimension='D1',
        body="Is the claim too broad, lacking in specifics, with terms like"
        "'all-natural', 'non-toxic', 'environmentally friendly', "
        "'eco-friendly', or 'eco-conscious' poorly defined?")
    Questao.objects.create(
        dimension='D1',
        body="Does the claim apply a false suggestion or certification-like "
        "image that misleads consumers into a legitimate green certification "
        "process?")
    Questao.objects.create(
        dimension='D1',
        body="Is the claim relevant in the contex? Is unimportant or "
        "unhelpful, in a way that it's obvious because exists a regulation "
        "from the authorities?")
    Questao.objects.create(
        dimension='D1',
        body="Does the claim risk distracting the consumer from the greater "
        "environmental impacts of the category as a whole, even if it may be "
        "true within the product category?")
    Questao.objects.create(
        dimension='D1',
        body="Is the claim false or untrue?")
    Questao.objects.create(
        dimension='D2',
        body="Does the product environmental communication suggest "
        "nature-evoking elements such as images using colors (e.g. green, "
        "blue), nature landscapes (e.g. mountains, forests, oceans)?")
    Questao.objects.create(
        dimension='D2',
        body="Does the product environmental communication suggest "
        "nature-evoking elements such as images using pictures of endangered "
        "species (e.g. pandas, dolphins) or renewable sources of energy (wind,"
        " sun)?")
    Questao.objects.create(
        dimension='D2',
        body="Does the product environmental communication suggest "
        "nature-evoking elements such as sounds (e.g. sea, birds)?")
    Questao.objects.create(
        dimension='D3',
        body="Does the claim belong to an inherently unsustainable business, "
        "promoting sustainable practices that are not representative neither "
        "for the business or the society?")
    Questao.objects.create(
        dimension='D3',
        body="Does the claim divert attention from sustainable issues, "
        "through the use of exaggerated achievements or present alternative "
        "programs that are not related to the main sustainability concern?")
    Questao.objects.create(
        dimension='D3',
        body="Does the claim try to influence regulations or governments in "
        "order to obtain benefits that affect sustainability due to the "
        "companies character of large taxpayers or employers?")
    Questao.objects.create(
        dimension='D3',
        body="Does the claim sustain environmental accomplishments or "
        "commitments that are already required by existing laws or "
        "regulations?")
    Questao.objects.create(
        dimension='D3',
        body=" Does the company take advantage of sustainability reports and "
        "their nature of one-way communication channel, in order to twist the "
        "truth or project a positive image in terms of CSR practices?")
    Questao.objects.create(
        dimension='D3',
        body="Does the claim reinforce a false hope?")
    Questao.objects.create(
        dimension='D3',
        body="Does the claim fabricate a treat or insecurity related to 'not "
        "buying in' on an organization practice?")
    Questao.objects.create(
        dimension='D3',
        body="Does the claim make a broken promise, guaranteeing that an "
        "organization practice will provide economic development to the "
        "community?")
    Questao.objects.create(
        dimension='D3',
        body="Does the claim does not speak directly to the communities most "
        "affected by its practices?")
    Questao.objects.create(
        dimension='D3',
        body="Does the claim distracts the public from the dangers caused by "
        "hazardous consequences of its practices?")
    Questao.objects.create(
        dimension='D4',
        body="Does the company environmental communication suggest "
        "nature-evoking elements such as images using colors (e.g. green, "
        "blue), nature landscapes (e.g. mountains, forests, oceans)?")
    Questao.objects.create(
        dimension='D4',
        body="Does the company environmental communication suggest "
        "nature-evoking elements such as images using pictures of endangered "
        "species (e.g. pandas, dolphins) or renewable sources of energy (wind,"
        " sun)?")
    Questao.objects.create(
        dimension='D4',
        body="Does the company environmental communication suggest "
        "nature-evoking elements such as sounds (e.g. sea, birds)?")
