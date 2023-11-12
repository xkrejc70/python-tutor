import React, { useState, useEffect } from 'react'

const App = () => {

  const [data, setData] = useState([{}])

  // TODO: try catch block
  useEffect(() => {
    fetch("/api").then(
      res => res.json()
    ).then(
      data => {
        setData(data)
      }
    ).catch(error => console.log(error))
  }, [])

  return (
    <div>
      
      {(typeof data.host === 'undefined') ? (
        <p>Loading...</p>
      ) : (
        <p>{data.host}</p>
      )}

    </div>
  )
}

export default App