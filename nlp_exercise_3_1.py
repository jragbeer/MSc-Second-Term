import nltk

wiki = """
The Toronto Maple Leafs (officially the Toronto Maple Leaf Hockey Club and often simply referred to as the Leafs) are a professional ice hockey team based in Toronto, Ontario. They are members of the Atlantic Division of the Eastern Conference of the National Hockey League (NHL). The club is owned by Maple Leaf Sports & Entertainment, Ltd. and are represented by Chairman Larry Tanenbaum. With an estimated value of US $1.45 billion in 2018 according to Forbes, the Maple Leafs are the second most valuable franchise in the NHL, after the New York Rangers. The Maple Leafs' broadcasting rights are split between BCE Inc. and Rogers Communications. For their first 14 seasons, the club played their home games at the Mutual Street Arena, before moving to Maple Leaf Gardens in 1931. The Maple Leafs moved to their present home, Scotiabank Arena (originally named the Air Canada Centre) in February 1999.

The club was founded in 1917, operating simply as Toronto and known then as the Toronto Arenas. Under new ownership, the club was renamed the Toronto St. Patricks in 1919. In 1927 the club was purchased by Conn Smythe and renamed the Maple Leafs. A member of the "Original Six", the club was one of six NHL teams to have endured through the period of League retrenchment during the Great Depression. The club has won thirteen Stanley Cup championships, second only to the 24 championships of the Montreal Canadiens. The Maple Leafs history includes two recognized dynasties, from 1947 to 1951; and from 1962 to 1967. Winning their last championship in 1967, the Maple Leafs' 50-season drought between championships is the longest current drought in the NHL. The Maple Leafs have developed rivalries with three NHL franchises, the Detroit Red Wings, the Montreal Canadiens, and the Ottawa Senators.

The Maple Leafs have retired the use of thirteen numbers in honour of nineteen players. In addition, a number of individuals who hold an association with the club have been inducted in the Hockey Hall of Fame. The Maple Leafs are presently affiliated with two minor league teams, the Toronto Marlies of the American Hockey League, and the Newfoundland Growlers of the ECHL.
Mascot
The Maple Leafs' mascot is Carlton the Bear, an anthropomorphic polar bear whose name and number (#60) comes from the location of Maple Leaf Gardens at 60 Carlton Street, where the Leafs played throughout much of their history. Carlton made his first public appearance on July 29, 1995. He later made his regular season appearance on October 10, 1995.

Minor league affiliates
The Maple Leafs are presently affiliated with two minor league teams, the Toronto Marlies of the American Hockey League and the Newfoundland Growlers of the ECHL. The Marlies play from Coca-Cola Coliseum in Toronto. Prior to its move to Coca-Cola Coliseum in 2005, the team was located in St. John's, Newfoundland and was known as the St. John's Maple Leafs. The Marlies originated from the New Brunswick Hawks, who later moved to St. Catherines, Newmarket, and St. John's, before finally moving to Toronto. The Marlies was named after the Toronto Marlboros, a junior hockey team named after the Duke of Marlborough. Founded in 1903, the Marlboros were sponsored by the Leafs from 1927 to 1989. The Marlboros constituted one of two junior hockey teams the Leafs formerly sponsored, the other being the Toronto St. Michael's Majors.

The Growlers are an ECHL team based in St. John's, Newfoundland. The Growlers became affiliated with the Maple Leafs and the Marlies before the 2018–19 season. Unlike the Marlies, the Growlers are not owned by the Leafs' parent company, but are instead owned by a local ownership group in St. John's called Deacon Investments LTD.

Ownership
The Maple Leafs is one of six professional sports teams owned by Maple Leaf Sports & Entertainment (MLSE). Initially ownership of the club was held by the Arena Gardens of Toronto, Limited; an ownership group fronted by Henry Pellatt, that owned and managed Arena Gardens. The club was named a permanent franchise in the League following its inaugural season, with team manager Charles Querrie, and the Arena Gardens treasurer Hubert Vearncombe as its owners. The Arena Company owned the club until 1919, when litigations from Eddie Livingstone forced the company to declare bankruptcy. Querrie brokered the sale of the Arena Garden's share to the owners of the amateur St. Patricks Hockey Club. Maintaining his shares in the club, Querrie fronted the new ownership group until 1927, when the club was put up for sale. Toronto Varsity Blues coach Conn Smythe put together an ownership group and purchased the franchise for $160,000. In 1929, Smythe decided, in the midst of the Great Depression, that the Maple Leafs needed a new arena. To finance it, Smythe launched Maple Leaf Gardens Limited (MLGL), a publicly traded management company to own both the Maple Leafs and the new arena, which was named Maple Leaf Gardens. Smythe traded his stake in the Leafs for shares in MLGL, and sold shares in the holding company to the public to help fund construction for the arena.

Although Smythe was the face of MLGL from its founding, he did not gain controlling interest in the company until 1947. Smythe remained MLGL's principal owner until 1961, when he sold 90 percent of his shares to an ownership group consisting of Harold Ballard, John Bassett and Stafford Smythe. Ballard became majority owner in February 1972, shortly following the death of Stafford Smythe. Ballard was the principal owner of MLGL until his death in 1990. The company remained a publicly traded company until 1998, when an ownership group fronted by Steve Stavro privatized the company by acquiring more than the 90 percent of stock necessary to force objecting shareholders out.

While initially primarily a hockey company, with ownership stakes in a number of junior hockey clubs including the Toronto Marlboros of the Ontario Hockey Association, the company later branched out to own the Hamilton Tiger-Cats of the Canadian Football League from the late 1970s to late 1980s. On February 12, 1998, MLGL purchased the Toronto Raptors of the National Basketball Association, who were constructing the then-Air Canada Centre. After MLGL acquired the Raptors, the company changed its name to MLSE. The company's portfolio has since expanded to include the Toronto FC of Major League Soccer, the Toronto Marlies of the AHL, the Toronto Argonauts of the Canadian Football League, and a 37.5 percent stake in Maple Leaf Square.

The present ownership structure emerged in 2012, after the Ontario Teachers' Pension Plan (the company's former principal owner) announced the sale of its 75 percent stake in MLSE to a consortium made up of Bell Canada and Rogers Communications, in a deal valued at $1.32 billion. As part of the sale, two numbered companies were created to jointly hold stock. This ownership structure ensures that, at the shareholder level, Rogers and Bell vote their overall 75 percent interest in the company together and thus decisions on the management of the company must be made by consensus between the two. A portion of Bell's share in MLSE is owned by its pension fund, in order to make Bell's share in MLSE under 30 percent. This was done so that Bell could retain its existing 18 percent interest in the Montreal Canadiens; as NHL rules prevent any shareholder that owns more than 30 percent of a team from holding an ownership position in another. The remaining 25 percent is owned by Larry Tanenbaum, who is also the chairman of MLSE.
"""

text1 = nltk.word_tokenize(wiki)
tagSent = nltk.pos_tag(text1)
print("Tagged sent: ", tagSent)

# Get chunks with repetitive occurrences of
# singular noun <NN> or Proper Noun Singular <NNP>+
chunkGram = "NP-CHUNK: {<NN>+|<NNP>+|<NNS>+|<NP>+|<NPS>+|}"
find = nltk.RegexpParser(chunkGram)
chunkTree = find.parse(tagSent)

print("\n:******* All the chunked noun phrases *******")
for subtree in chunkTree.subtrees():
    if subtree.label() == 'NP-CHUNK':
        finalChunk = ""
        for (w, tag) in subtree.leaves():
            finalChunk = finalChunk + " " + w
        print(finalChunk)

chunkGram = "NP-CHUNK: {<VB>+|<VBG>+|<VBD>+|<VBZ>+|<VBN>+|<VH>+|<VBP>+|<VHD>+|<VHG>+|<VHN>+|<VHP>+|<VHZ>+|<VV>+|<VVD>+|<VVP>+|<VVN>+|<VVG>+}"
find = nltk.RegexpParser(chunkGram)
chunkTree = find.parse(tagSent)

print("\n:******* All the chunked verb phrases *******")
for subtree in chunkTree.subtrees():
    if subtree.label() == 'NP-CHUNK':
        finalChunk = ""
        for (w, tag) in subtree.leaves():
            finalChunk = finalChunk + " " + w
        print(finalChunk)

chunkGram = "NP-CHUNK: {<DT>+|<JJS>+|<NNS>+}"
find = nltk.RegexpParser(chunkGram)
chunkTree = find.parse(tagSent)

print("\n:******* All the chunked Det/Superlative/Noun (plural) phrases *******")
for subtree in chunkTree.subtrees():
    if subtree.label() == 'NP-CHUNK':
        finalChunk = ""
        for (w, tag) in subtree.leaves():
            finalChunk = finalChunk + " " + w
        print(finalChunk)