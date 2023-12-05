open System 
open System.IO
open System.Collections.Generic

type Card =
    {
        ID: int
        WinningNumbers: int list
        MatchNumbers: int list
    }

module Card =
    let buildFromData (id: int) (win: list<int>) (matching: list<int>) =
        {
            ID = id
            WinningNumbers = win
            MatchNumbers = matching
        }
    
    let toString (card: Card) =
        printfn "ID: %i" card.ID
        for win in card.WinningNumbers do
            printf "%i " win 
        printfn ""
        for matching in card.MatchNumbers do 
            printf "%i " matching
        printfn ""
        printfn "-----------------------"


let buildCards (strings: string array) : list<Card> =
    let mutable cards: list<Card> = []

    for s in strings do 
        let stringSplittedAtId = s.Split(":")

        let idParts = stringSplittedAtId.[0].Split(" ")
        let id = int (idParts[idParts.Length - 1])

        let stringSplittedAtCard = stringSplittedAtId.[1].Split("|") |> Array.map (fun s -> s.Trim())

        let winningCards = 
            stringSplittedAtCard.[0].Split(" ") 
            |> Array.filter (fun s -> s <> "") 
            |> Array.map int
            |> Array.toList 

        let test = stringSplittedAtCard.[1].Split(" ") |> Array.filter (fun s -> s <> "") |> Array.map int |> Array.toList

        let matchCards = 
            stringSplittedAtCard.[1].Split(" ")  
            |> Array.filter (fun s -> s <> "") 
            |> Array.map int  
            |> Array.toList

        let card = Card.buildFromData  id winningCards matchCards
        cards <- cards |> List.append [card]
    cards

let determinePoints (cards: Card list) = 
    let mutable totalPoints = 0

    for card in cards do 
        let mutable hits = 0   
        let winningNumbers = card.WinningNumbers
        let matchingNumbers = card.MatchNumbers

        for number in matchingNumbers do
            if List.contains number winningNumbers then
                hits <- hits + 1
        let points = pown 2 (hits - 1)
        totalPoints <- totalPoints + points
    totalPoints       

let countWonCards (cards: list<Card>) =
    let cards = List.rev cards
    
    let dict = new Dictionary<Card, int>()
    for card in cards do 
        dict.Add(card, 1)
    
    for card in cards do

        let mutable hits = 0   
        let winningNumbers = card.WinningNumbers
        let matchingNumbers = card.MatchNumbers

        for number in matchingNumbers do
            if List.contains number winningNumbers then
                hits <- hits + 1

        for j in 0..hits-1 do
            // dict.["everything"] <- 42
            let nextCard = cards[card.ID+j]
            dict[nextCard] <- dict[nextCard] + dict[card]

    let mutable sum = 0
    for entry in dict do 
        sum <- sum + entry.Value
    sum

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

            let part1 = filepath |> File.ReadAllLines |> buildCards |> determinePoints
            let part2 = filepath |> File.ReadAllLines |> buildCards |> countWonCards
                        
            printfn "Part 1: %i" part1
            printfn "Part 2: %i" part2
            0
        else
            printfn "File does not exist!"
            2