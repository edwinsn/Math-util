function areInverses(M){
    
    let e = findE(M)
    console.log(e)
    return M.every(  (row)=>  row.some( element=>element===e )  )
}

function findE(M){
    
    let e = false
    
    M.some( (row, rowIndex)=>{
        
        let isIdentity= row.every((e,i)=>{
            return e===i
            })
        if(isIdentity) e=rowIndex
        return isIdentity
    })
    
    return e
}

let M = [[0,1,2],[1,1,0],[0,1,1]]
console.log(areInverses(M))

M = [[0,1,2],[1,1,0],[2,1,2]]
console.log(areInverses(M))
