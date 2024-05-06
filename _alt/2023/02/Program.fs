open System
open System.IO

type Draw =
    {
        Reds: int
        Greens: int
        Blues: int
    }

type GameRound =
    {
        ID: int
        Draws: Draw list
    }

module Draw =
      let fromList (colorNumbers: int list) = 
           {
           Reds = colorNumbers.[0]
           Greens = colorNumbers.[1]
           Blues = colorNumbers.[2]
           }

module GameRound = 
    let fromData (id: int) (draws: Draw list) = 
        {
            ID = id
            Draws = draws
        }

let buildAllGameRounds (filepath: string) =
    // Alle Zeilen auslesen
    let rows = filepath |> File.ReadAllLines 
    // An Game ID splitten
    let gameRoundsWithID = rows |> Array.map (fun row -> row.Split(":"))

    // Rueckgaebe initialisieren
    let mutable gameRounds: GameRound list = []

    // Ueber alle Zeilen iterieren
    for i in 0..gameRoundsWithID.Length - 1 do 
        // Ziehungen dieser Zeile initialisieren
        let mutable draws = []

        let id = i
        
        // Naechste Runde in einzelne Ziehungen splitten
        let nextRound = gameRoundsWithID[i][1]
        let splittedGameRounds = nextRound.Split(";")

        for splittedGameRound in splittedGameRounds do
            // Die naechste Ziehung holen
            let drawsInThisRound = splittedGameRound.Split(";")
            
            // Ziehung in das Format "[<reds>, <greens>, <blues>]" ueberfuehren.
            for draw in drawsInThisRound do
                let colorsInThisRound = draw.Split(",")
                let mutable colors = [0; 0; 0]
                for color in colorsInThisRound do
                    let elements = color.Split(" ")
                    let colorNumber = int elements[1]
                    let colorName = elements[2]
                    if colorName = "red" then 
                        colors <- [colors.[0] + colorNumber; colors.[1]; colors.[2]]
                    if colorName = "green" then 
                        colors <- [colors.[0]; colors.[1] + colorNumber; colors.[2]]
                    if colorName = "blue" then
                        colors <- [colors.[0]; colors.[1]; colors.[2] + colorNumber]
                // Ziehungs-Type aufbauen und den Ziehungen hinzufuegen
                let drawType: Draw = Draw.fromList(colors)
                draws <- List.append [drawType] draws
        
        // Reihenfolge der Liste invertieren, damit sie zur urspruenglichen Reihenfolge passt.
        draws <- List.rev draws

        // GameRound-Type bauen
        let gameRound = GameRound.fromData id draws

        // GameRounds aktualisieren
        gameRounds <- List.append [gameRound] gameRounds
    // Reihenfolge der Liste invertieren, damit sie zur urspruenglichen Reihenfolge passt.
    gameRounds <- List.rev gameRounds
    gameRounds

let sumAllIDsWhereGameIsPossible (games: GameRound list) =
    let colorsToCheck = [12; 13; 14]
    let mutable sumOfIDs = 0 

    for game in games do 
        let mutable isPossible = true
        let id = game.ID + 1
        let draws = game.Draws

        for draw in draws do
            if draw.Reds > colorsToCheck.[0] || draw.Greens > colorsToCheck.[1] || draw.Blues > colorsToCheck.[2] then 
                isPossible <- false
        if isPossible then
            sumOfIDs <- sumOfIDs + id 
    sumOfIDs

let sumAllPowersPlayingWithMinimumCubes (games: GameRound list) =
    let mutable sumOfPowers = 0
    
    for game in games do
        let mutable minReds = 0
        let mutable minGreens = 0
        let mutable minBlues = 0

        let draws = game.Draws

        for draw in draws do
            if draw.Reds > minReds then 
                minReds <- draw.Reds
            if draw.Greens > minGreens then 
                minGreens <- draw.Greens
            if draw.Blues > minBlues then 
                minBlues <- draw.Blues
        
        sumOfPowers <- sumOfPowers + minReds*minGreens*minBlues
    sumOfPowers


let fileIsGivenAndExists (arguments: String array) (filepath: string) =
    arguments.Length = 1 && File.Exists filepath

[<EntryPoint>]
let main argv =
    if argv.Length = 0 then
        printfn "Please specify a file!"
        1
    elif argv.Length > 1 then
        printfn "More than one file given!"
        2
    else
        let filepath = argv.[0]

        if filepath |> fileIsGivenAndExists argv then
            printfn "Processing %s" filepath
            let games = filepath |> buildAllGameRounds
            let sumIDsPossible = games |> sumAllIDsWhereGameIsPossible
            let sumOfPowers = games |> sumAllPowersPlayingWithMinimumCubes
            
            printfn "Part 1: %i" sumIDsPossible
            printfn "Part 2: %i" sumOfPowers
            0
        else
            printfn "File does not exist!"
            2
