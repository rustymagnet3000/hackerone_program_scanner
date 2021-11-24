from typing import NamedTuple

filename = 'companies.txt'


class H1Program(NamedTuple):
    """
      blueprint for H1Program
    """
    id: int
    name: str
    offers_bounties: bool
    triage_active: bool

#H1Program = namedtuple('H1Program', ['id', 'name': str, 'offers_bounties', 'triage_active'])
# class H1Program:
    # def __init__(self, h1_id, name, offers_bounties, triage_active):
    #     self.id: int = int(h1_id)
    #     self.name: str = name
    #     self.offers_bounties: bool = bool(offers_bounties)
    #     self.triage_active: bool = bool(triage_active)