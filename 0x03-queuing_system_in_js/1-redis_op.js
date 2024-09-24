import { createClient, print } from 'redis';

const client = createClient();

client.connect()
  .then(() => {
    console.log('Redis client connected to the server');
  })
  .catch((err) => {
    console.log(`Redis client not connected to the server: ${err}`);
  });

// function setNewSchool(schoolName, value) {
//   client.set(schoolName, value, print)
// }

// function displaySchoolValue(schoolName) {
//   client.get(schoolName, (err, result) => {
//     if (err){
//       console.log(err);
//       throw err;
//     }
//     console.log(result);
//   })
// }
function setNewSchool (schoolName, value) {
  client.set(schoolName, value, print);
}

function displaySchoolValue (schoolName) {
  client.get(schoolName, function (error, result) {
    if (error) {
      console.log(error);
      throw error;
    }
    console.log(result);
  });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
