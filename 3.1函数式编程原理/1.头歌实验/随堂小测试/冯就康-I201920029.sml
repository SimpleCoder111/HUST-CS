fun subsetSumOption (L, s) = 
  let 
    fun subset [] _ = NONE
      | subset (x::xs) sum = 
        if x = sum then SOME [x]
        else 
          let 
            val withX = subset xs (sum - x)
            val withoutX = subset xs sum
          in
            case withX of 
              SOME lst => SOME (x::lst)
            | NONE => withoutX
          end
  in
    subset L s
  end;