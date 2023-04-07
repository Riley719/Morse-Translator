function click(morse){
    let morsecode = [   [".-", "a"], ["-...", "b"], ["-.-.", "c"], ["-..", "d"], [".", "e"], 
    ["..-.", "f"], ["--.", "g"], ["....", "h"], ["..", "i"], [".---", "j"], 
    ["-.-", "k"], [".-..", "l"], ["--", "m"], ["-.", "n"], ["---", "o"], 
    [".--.", "p"], ["--.-", "q"], [".-.", "r"], ["...", "s"], ["-", "t"], 
    ["..-", "u"], ["...-", "v"], [".--", "w"], ["-..-", "x"], ["-.--", "y"], 
    ["--..", "z"]]

    let hako = [...morse]
    let trans = []
    let code = ""
    let translation = ""

    for(var i=0; i < hako.length; i++){
        if(hako[i] == "･"){
            hako[i] = "."
        }
        if(hako[i] == "ｰ"){
            hako[i] = "-"
        }
    }

    for(var i=0; i < hako.length; i++){
        if(hako[i] !== " " && i !== hako.length){
            code += hako[i]
        }
        else{
            trans.push(code)
            code = ""
        }
    }
    trans.push(code)

    var i = 0
    while(i < trans.length){
        if(trans[i] == ""){
            translation += " "
            i += 2
        }
        else{
            for(var j=0; j < 26; j++){
                if(trans[i] == morsecode[j][0]){
                    translation += morsecode[j][1]
                }
            }
            i += 1
        }
    }

    var end = document.getElementById("end")
    end.innerHTML = translation



}