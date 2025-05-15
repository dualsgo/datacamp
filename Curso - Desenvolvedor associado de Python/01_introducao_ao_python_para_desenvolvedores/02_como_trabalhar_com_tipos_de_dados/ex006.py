"""Trabalhando com dicionários
Você tem estado ocupado, adicionando mais artistas e músicas ao seu dicionário playlist em preparação para a festa!

Como lembrete, ele contém nomes de artistas como chaves e nomes de músicas como valores.

Neste exercício, você acessará partes do dicionário e adicionará um novo artista e uma nova música.

Instruções
100 XP
Imprima o nome da música naplaylist que é do artista "Coldplay".
Adicione um novo par chave-valor à playlist, em que a chave é "Usher" e o valor é "Yeah!".
Imprima somente as músicas na playlist."""

playlist = {
	'The Weeknd': 'Blinding Lights',
	'Drake': 'One Dance',
	'Mark Ronson': 'Uptown Funk',
	'The Chainsmokers': 'Closer',
	'Calvin Harris': 'One Kiss',
	'The Killers': 'Mr. Brightside',
	'Oasis': 'Wonderwall',
	'Rihanna': 'We Found Love',
	'Coldplay': 'Paradise',
	'Usher': 'Yeah!'
}


# Print the song by Coldplay
print(playlist["Coldplay"])

# Add a new song
playlist["Usher"] = "Yeah!"

# Print the songs in the playlist
print(playlist.values())