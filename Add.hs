import Data.Char

main = do
    putStr("Please provide an integer: ")
    n <- getLine
    let sum = foldl (+) 0 (map digitToInt n)
    putStrLn(n ++ " reduces to " ++ show(sum))
