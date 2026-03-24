
async def get_recommendations ( mood: str, language: str) : 

    #mockapi
    songs = [
        {
            "id" : "1",
            "title" : "Happy Song 1",
            "artist" : "Artist A",
            "mood" : "happy",
            "language" : "english" ,
        },
        {
            "id" : "2",
            "title" : "Sad Song 1",
            "artist" : "Artist B",
            "mood" : "sad",
            "language" : "english" ,
        },
        {
            "id" : "3",
            "title" : "Calm Song 1",
            "artist" : "Artist C",
            "mood" : "calm",
            "language" : "english" ,
        },

    ]

    filtered_songs = [
        song for song in songs if song["language"] == language and song["mood"] == mood   
    ]

    return filtered_songs