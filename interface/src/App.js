import React, { useState , useEffect} from 'react'; 

function App() {

    const [data ,setData] = useState([{}])
        useEffect(() => {
            fetch("/endTOEndEncryption").then(
                res => res.json()
    
            ).then(
                data =>{
                    setData(data)
                    console.log(data)
                }
            )
        },[])

    
    return (
        <div>
            {(typeof data.endTOEndEncryption === 'undefined') ? (
                <p>Loading ...</p>
            ):(
                data.endTOEndEncryption.map((a, i) =>(
                    <p key={i}>{a}</p>
                ))

            )}

        </div>
    )
}

export default App
