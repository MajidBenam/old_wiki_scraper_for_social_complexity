SC_VAR_DEFINITIONS = {'ra': "The name of the research assistant or associate who coded the data. If more than one RA made a substantial contribution, list all via separate entries.",
'polity_territory': "Talking about Social Scale, Polity territory is coded in squared kilometers.",
'polity_population': "Talking about Social Scale, Polity Population is the estimated population of the polity; can change as a result of both adding/losing new territories or by population growth/decline within a region",
'population_of_the_largest_settlement': "Talking about Social Scale, Population of the largest settlement is the estimated population of the largest settlement of the polity. Note that the largest settlement could be different from the capital (coded under General Variables). If possible, indicate the dynamics (that is, how population changed during the temporal period of the polity). Note that we are also building a city database - you should consult it as it may already have the needed data.",
'settlement_hierarchy': "Talking about Hierarchical Complexity, Settlement hierarchy records (in levels) the hierarchy of not just settlement sizes, but also their complexity as reflected in different roles they play within the (quasi)polity. As settlements become more populous they acquire more complex functions: transportational (e.g. port); economic (e.g. market); administrative (e.g. storehouse, local government building); cultural (e.g. theatre); religious (e.g. temple), utilitarian (e.g. hospital), monumental (e.g. statues, plazas). Example: (1) Large City (monumental structures, theatre, market, hospital, central government buildings) (2) City (market, theatre, regional government buildings) (3) Large Town (market, administrative buildings) (4) Town (administrative buildings, storehouse)) (5) Village (shrine) (6) Hamlet (residential only). In the narrative paragraph explain the different levels and list their functions. Provide a (crude) estimate of population sizes. For example, Large Town (market, temple, administrative buildings): 2,000-5,000 inhabitants.",
'administrative_level': "Talking about Hierarchical Complexity, Administrative levels records the administrative levels of a polity. An example of hierarchy for a state society could be (1) the overall ruler, (2) provincial/regional governors, (3) district heads, (4) town mayors, (5) village heads. Note that unlike in settlement hierarchy, here you code people hierarchy. Do not simply copy settlement hierarchy data here. For archaeological polities, you will usually code as 'unknown', unless experts identified ranks of chiefs or officials independently of the settlement hierarchy. Note: Often there are more than one concurrent administrative hierarchy. In the example above the hierarchy refers to the territorial government. In addition, the ruler may have a hierarchically organized central bureaucracy located in the capital. For example, (4)the overall ruler, (3) chiefs of various ministries, (2) midlevel bureaucrats, (1) scribes and clerks. In the narrative paragraph detail what is known about both hierarchies. The machine-readable code should reflect the largest number (the longer chain of command).",
'religious_level': "Talking about Hierarchical Complexity, Religious levels records the Religious levels of a polity. Same principle as with Administrative levels. Start with the head of the official cult (if present) coded as: level 1, and work down to the local priest.",
'military_level': "Talking about Hierarchical Complexity, Military levels records the Military levels of a polity. Same principle as with Administrative levels. Start with the commander-in-chief coded as: level 1, and work down to the private. Even in primitive societies such as simple chiefdoms it is often possible to distinguish at least two levels – a commander and soldiers. A complex chiefdom would be coded three levels. The presence of warrior burials might be the basis for inferring the existence of a military organization. (The lowest military level is always the individual soldier).",

'professional_military_officer': "Talking about Professions, Professional military officers refer to Full-time Professional military officers.",
'professional_soldier': "Talking about Professions, Professional soldiers refer to Full-time Professional soldiers.",
'professional_priesthood': "Talking about Professions, Professional priesthood refers to Full-time Professional priesthood.",


'full_time_bureaucrat': "Talking about Bureaucracy characteristics, Full-time bureaucrats refer to Full-time administrative specialists. Code this absent if administrative duties are performed by generalists such as chiefs and subchiefs. Also code it absent if state officials perform multiple functions, e.g. combining administrative tasks with military duties. Note that this variable shouldn't be coded 'present' only on the basis of the presence of specialized government buildings; there must be some additional evidence of functional specialization in government.",
'examination_system': "Talking about Bureaucracy characteristics, The paradigmatic example of an Examination system is the Chinese imperial system.",
'merit_promotion': "Talking about Bureaucracy characteristics, Merit promotion is coded present if there are regular, institutionalized procedures for promotion based on performance. When exceptional individuals are promoted to the top ranks, in the absence of institutionalized procedures, we code it under institution and equity variables",
'specialized_government_building': "Talking about Bureaucracy characteristics, These buildings are where administrative officials are located, and must be distinct from the ruler's palace. They may be used for document storage, registration offices, minting money, etc. Defense structures also are not coded here (see Military). State-owned/operated workshop should also not be coded here.",

'formal_legal_code': "Talking about Law, Formal legal code refers to legal code usually, but not always written down. If not written down, code it 'present' when a uniform legal system is established by oral transmission (e.g., officials are taught the rules, or the laws are announced in a public space). Provide a short description",
'judge': "Talking about Law, judges refers only to full-time professional judges",
'court': "Talking about Law, courts are buildings specialized for legal proceedings only.",
'professional_lawyer': "Talking about Law, NO_DESCRIPTIONS_IN_CODEBOOK.",


'irrigation_system': "Talking about Specialized Buildings, irrigation systems are polity owned (which includes owned by the community, or the state), NO_DESCRIPTIONS_IN_CODEBOOK",
'drinking_water_supply_system': "Talking about Specialized Buildings, drinking water supply systems are polity owned (which includes owned by the community, or the state), NO_DESCRIPTIONS_IN_CODEBOOK",
'market': "Talking about Specialized Buildings, markets are polity owned (which includes owned by the community, or the state), NO_DESCRIPTIONS_IN_CODEBOOK",
'food_storage_site': "Talking about Specialized Buildings, food storage sites are polity owned (which  includes owned by the community, or the state), NO_DESCRIPTIONS_IN_CODEBOOK",


'road': "Talking about Transport infrastructure, roads refers to deliberately constructed roads that connect settlements or other sites. It excludes streets/accessways within settlements and paths between settlements that develop through repeated use.",
'bridge': "Talking about Transport infrastructure, bridges refers to bridges built and/or maintained by the polity (that is, code 'present' even if the polity did not build a bridge, but devotes resources to maintaining it).",
'canal': "Talking about Transport infrastructure, canals refers to canals built and/or maintained by the polity (that is, code 'present' even if the polity did not build a canal, but devotes resources to maintaining it).",
'port': "Talking about Transport infrastructure, Ports include river ports. Direct historical or archaeological evidence of Ports is absent when no port has been excavated or all evidence of such has been obliterated. Indirect historical or archaeological data is absent when there is no evidence that suggests that the polity engaged in maritime or riverine trade, conflict, or transportation, such as evidence of merchant shipping, administrative records of customs duties, or evidence that at the same period of time a trading relation in the region had a port (for example, due to natural processes, there is little evidence of ancient ports in delta Egypt at a time we know there was a timber trade with the Levant). When evidence for the variable itself is available the code is 'present.' When other forms of evidence suggests the existence of the variable (or not) the code may be 'inferred present' (or 'inferred absent'). When indirect evidence is not available the code will be either absent, temporal uncertainty, suspected unknown, or unknown.",
'mines_or_quarry': "Talking about Special purpose sites, NO_DESCRIPTIONS_IN_CODEBOOK",


'mnemonic_device': "Talking about Writing Systems, Mnemonic devices are: For example, tallies",
'nonwritten_record': "Talking about Writing Systems, Nonwritten Records are more extensive than mnemonics, but don't utilize script. Example: quipu; seals and stamps",
'written_record': "Talking about Writing Systems, Written records are more than short and fragmentary inscriptions, such as found on tombs or runic stones. There must be several sentences strung together, at the very minimum. For example, royal proclamations from Mesopotamia and Egypt qualify as written records",
'script': "Talking about Writing Systems, script is as indicated at least by fragmentary inscriptions (note that if written records are present, then so is script)",
'non_phonetic_writing': "Talking about Writing Systems, this refers to the kind of script",
'phonetic_alphabetic_writing': "Talking about Writing Systems, this refers to the kind of script",

'lists_tables_and_classification': "Talking about Kinds of Written Documents, NO_DESCRIPTIONS_IN_CODEBOOK",
'calendar': "Talking about Kinds of Written Documents, NO_DESCRIPTIONS_IN_CODEBOOK",
'sacred_text': "Talking about Kinds of Written Documents, Sacred Texts originate from supernatural agents (deities), or are directly inspired by them.",
'religious_literature':  "Talking about Kinds of Written Documents, Religious literature differs from the sacred texts. For example, it may provide commentary on the sacred texts, or advice on how to live a virtuous life.",
'practical_literature':  "Talking about Kinds of Written Documents, Practical literature refers to texts written with the aim of providing guidance on a certain topic, for example manuals on agriculture, warfare, or cooking. Letters do not count as practical literature.",
'history': "Talking about Kinds of Written Documents, NO_DESCRIPTIONS_IN_CODEBOOK",
'philosophy': "Talking about Kinds of Written Documents, NO_DESCRIPTIONS_IN_CODEBOOK",
'scientific_literature': "Talking about Kinds of Written Documents, Scientific literature includes mathematics, natural sciences, social sciences",
'fiction': "Talking about Kinds of Written Documents, fiction includes poetry.",

'article': "Talking about forms of money, articles are items that have both a regular use and are used as money (example: axes, cattle, measures of grain, ingots of non-precious metals)",
'token': "Talking about forms of money, tokens, unlike articles, are used only for exchange, and unlike coins, are not manufactured (example: cowries)",
'precious_metal': "Talking about forms of money, Precious metals are non-coined silver, gold, platinum",
'foreign_coin': "NO_DESCRIPTIONS_IN_CODEBOOK",
'indigenous_coin': "NO_DESCRIPTIONS_IN_CODEBOOK",
'paper_currency': "Paper currency or another kind of fiat money. Note that this only refers to indigenously produced paper currency. Code absent if colonial money is used.",
'courier': "Full-time professional couriers.",
'postal_station': "Talking about postal sytems, Postal stations are specialized buildings exclusively devoted to the postal service. If there is a special building that has other functions than a postal station, we still code postal station as present. The intent is to capture additional infrastructure beyond having a corps of messengers.",
'general_postal_service': "Talking about postal sytems, 'General postal service' refers to a postal service that not only serves the ruler's needs, but carries mail for private citizens."}




SC_VAR_SUBSECTIONS = {'ra': "staff",
'polity_territory': "Social Scale",
'polity_population': "Social Scale",
'population_of_the_largest_settlement': "Social Scale",
'settlement_hierarchy': "Hierarchical Complexity",
'administrative_level': "Hierarchical Complexity",
'religious_level': "Hierarchical Complexity",
'military_level': "Hierarchical Complexity",

'professional_military_officer': "Professions",
'professional_soldier': "Professions",
'professional_priesthood': "Professions",


'full_time_bureaucrat': "Bureaucracy characteristics",
'examination_system': "Bureaucracy characteristics",
'merit_promotion': " Bureaucracy characteristics",
'specialized_government_building': " Bureaucracy characteristics",

'formal_legal_code': "Law",
'judge': "Law",
'court': "Law",
'professional_lawyer': "Law",


'irrigation_system': "Specialized Buildings",
'drinking_water_supply_system': "Specialized Buildings",
'market': "Specialized Buildings",
'food_storage_site': "Specialized Buildings",


'road': "Transport infrastructure",
'bridge': "Transport infrastructure",
'canal': "Transport infrastructure",
'port': "Transport infrastructure",

'mines_or_quarry': "Special purpose sites",

'mnemonic_device': "Writing Systems",
'nonwritten_record': "Writing Systems",
'written_record': "Writing Systems",
'script': "Writing Systems",
'non_phonetic_writing': "Writing Systems",
'phonetic_alphabetic_writing': "Writing Systems",

'lists_tables_and_classification': "Kinds of Written Documents",
'calendar': "Kinds of Written Documents",
'sacred_text': "Kinds of Written Documents",
'religious_literature':  "Kinds of Written Documents",
'practical_literature':  "Kinds of Written Documents",
'history': "Kinds of Written Documents",
'philosophy': "Kinds of Written Documents",
'scientific_literature': "Kinds of Written Documents",
'fiction': "Kinds of Written Documents",

'article': "Forms of money",
'token': "Forms of money",
'precious_metal': "Forms of money",
'foreign_coin': "Forms of money",
'indigenous_coin': "Forms of money",
'paper_currency': "Forms of money",


'courier': "Postal sytems",
'postal_station': "Postal sytems",
'general_postal_service': "Postal sytems"}