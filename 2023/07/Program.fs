open System
open System.IO
open System.Collections.Generic

let cardMapping: Dictionary<string, int> = new Dictionary<string, int>()
cardMapping.Add("2", 2)
cardMapping.Add("3", 3)
cardMapping.Add("4", 4)
cardMapping.Add("5", 5)
cardMapping.Add("6", 6)
cardMapping.Add("7", 7)
cardMapping.Add("8", 8)
cardMapping.Add("9", 9)
cardMapping.Add("T", 10)
cardMapping.Add("J", 11)
cardMapping.Add("Q", 12)
cardMapping.Add("K", 13)
cardMapping.Add("A", 14)

type CamelCardHand = 
    {
        Cards: list<int>
        Bid: int
    }

module CamelCardHand = 

    let fromData (cards: string) (bid: int) =
        let valuesAsChars = cards.ToCharArray() |> Array.map (fun symbol -> cardMapping[string symbol]) |> Array.toList |> List.sort
        {
            Cards = valuesAsChars
            Bid = bid
        } 
    
    let toString (card: CamelCardHand) =
        printf "Cards: "
        for i in card.Cards do 
            printf "%i " i
        printfn ""
        printfn "Bid: %i" card.Bid
        printfn "-------------------------------"


let buildCamelCardHandsFromInput (filepath: string) = 
    let lines = filepath |> File.ReadAllLines
    let mutable cards: list<CamelCardHand> = []

    for line in lines do
        let splittedLine = line.Split(" ")
        cards <- cards |> List.append [CamelCardHand.fromData splittedLine.[0] (splittedLine.[1] |> int)]
    cards <- cards |> List.rev

    for i in 0..cards.Length-1 do 
        CamelCardHand.toString cards.[i]

    cards 


let calculateTotalWinnings (hands: list<CamelCardHand>) = 
    -2


let fileIsGivenAndExists (arguments: String array) (filepath: string) = 
    arguments.Length = 1 && File.Exists filepath

[<EntryPoint>]
let main (argv: String array) = 
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

            let part1 = filepath |> buildCamelCardHandsFromInput |> calculateTotalWinnings
            let part2 = -1
            
            printfn "Part 1: %i" part1
            printfn "Part 2: %i" part2

            0
        else    
            printfn "File does not exist!"
            2 