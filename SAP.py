#! /Library/Frameworks/Python.framework/Versions/3.5/bin/python3
import plotly.plotly as py
import plotly.graph_objs as go
import spotipy
import json

import spotipy.util as util
import spotipy.oauth2 as oauth2
import matplotlib.pyplot as plt
import networkx as nx
from spotipy.oauth2 import SpotifyClientCredentials

username = str(input("Spotify username"))
scope = 'playlist-read-private'
clientID = "77e5b6e37ecb45dd8351eb0cd54f6242"
clientSecret = "aba2675b3e2148da8405780022b527e0"
clientUri = "http://localhost"
artistVertices = []
artistEdges = []

client_credentials_manager = SpotifyClientCredentials(
    client_id=clientID, client_secret=clientSecret)
spotify = spotipy.Spotify(
    client_credentials_manager=client_credentials_manager)


def createArtistEdges(artistName, artistDict, edgeList):
    for id, name in artistDict.items():
        if (artistName, name) not in edgeList:
            edgeList.append((artistName, name))
    return edgeList


def createArtistVertices(verticeList, artistsDict):
    for id, name in artistDict.items():
        if name not in verticeList:
            verticeList.append(name)
    return verticeList


def addEdgesVertices(relatedArtists):
    tempArtists = relatedArtists['artists']
    artists = {}
    for artist in tempArtists:
        artists.update({artist['uri']: artist['name']})
    return artists


artistName = str(input("Search for artist name\n"))
results = spotify.search(q="{name}".format(
    name=artistName), type="artist")
artists = results['artists']['items']
for artist in artists:
    print(artist['name'], artist['id'])

index = int(input('Which one?'))
artistID = artists[index]['id']
artistName = artists[index]['name']
degree = int(input("How many degrees down do you want to search"))
overallArtists = {}


def plot():
    relatedArtists = spotify.artist_related_artists(id)
    artistDict = addEdgesVertices(relatedArtists)
    artistVertices = createArtistVertices(artistVertices, artistDict)
    artistEdges = createArtistEdges(name, artistDict, artistEdges)


while degree > 0:
    relatedArtists = spotify.artist_related_artists(artistID)
    artistDict = addEdgesVertices(relatedArtists)
    artistVertices = createArtistVertices(artistVertices, artistDict)
    artistEdges = createArtistEdges(artistName, artistDict, artistEdges)
    overallArtists.update(artistDict)
    artistDict = overallArtists.copy()
    for id, name in artistDict.items():
        relatedArtists = spotify.artist_related_artists(id)
        artistDict = addEdgesVertices(relatedArtists)
        artistVertices = createArtistVertices(artistVertices, artistDict)
        artistEdges = createArtistEdges(name, artistDict, artistEdges)
        overallArtists.update(artistDict)
    degree -= 1


G = nx.Graph()

G.add_nodes_from(artistVertices)
G.add_edges_from(artistEdges)

nx.draw(G, with_labels=True, font_weight='bold')
plt.show()
