import React, { useEffect, useState } from 'react'

const Dashboard = () => {
  const [dbName, setDbName] = useState({});
   useEffect(() => {
    fetch("/db")
      .then(res => res.json()
        .then(data => {
          setDbName((data))
        }))
    }, []);

  return (
    <div>
      The list of DBs present is
      {
        Object.keys(dbName).map(key => {
          const dbz = dbName[key]
          const items = []
          console.log(dbz)
          let len = dbz.length;
          for(let i=0; i<len; i++){
            items.push(<li key={i}>{dbz[i]}</li>)
          }
          return items
        })
      }
    </div>
  );
}

export default Dashboard
