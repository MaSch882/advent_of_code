﻿open System
open System.IO

type Node = 
    {
        Name: string
        Left: string
        Right: string
    }

module Node = 

    let fromData (name: string) (left: string) (right: string) =
        {
            Name = name
            Left = left
            Right = right
        }

    let toString (node: Node) = 
        printfn "(%s) = (%s, %s)" node.Name node.Left node.Right


let buildSequence (filepath: string) = 
    let lines = filepath |> File.ReadAllLines |> Array.filter (fun s -> s <> "")

    let sequence = lines.[0]
    sequence

let buildNodes (filepath: string) = 
    let lines = filepath |> File.ReadAllLines |> Array.filter (fun s -> s <> "")

    let mutable extractedNotes : list<Node> = [] 

    for i in 1..lines.Length - 1 do 
        let line = lines.[i]
        let lineAsChars = line.ToCharArray() |> Array.map string

        let name = lineAsChars.[0] + lineAsChars.[1] + lineAsChars.[2]
        let left = lineAsChars.[7] + lineAsChars.[8] + lineAsChars.[9]
        let right = lineAsChars.[12] + lineAsChars.[13] + lineAsChars.[14]

        let node = Node.fromData name left right
        extractedNotes <- extractedNotes |> List.append [node]

    extractedNotes <- extractedNotes |> List.rev
    extractedNotes


let countStepsToReachEnd (seq: string) (n: list<Node>) = 
    let mutable steps = 0

    let sequence = seq
    let nodes = n

    let sequenceAsChars = sequence.ToCharArray() |> Array.map string

    let mutable currentNode = nodes |> List.find (fun node -> node.Name = "AAA")
    let mutable nextInput = sequenceAsChars.[0]

    while currentNode.Name <> "ZZZ" do 
        if nextInput = "L" then
            currentNode <- nodes |> List.find (fun node -> node.Name = currentNode.Left)
            steps <- steps + 1
            nextInput <- sequenceAsChars.[steps % sequence.Length] 
        else 
            currentNode <- nodes |> List.find (fun node -> node.Name = currentNode.Right)
            steps <- steps + 1
            nextInput <- sequenceAsChars.[steps % sequence.Length] 
    steps


    

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

            let part1 = countStepsToReachEnd (filepath |> buildSequence) (filepath |> buildNodes)
            let part2 = -1
            
            printfn "Part 1: %i" part1
            printfn "Part 2: %i" part2

            0
        else    
            printfn "File does not exist!"
            2 