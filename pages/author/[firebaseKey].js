/* eslint-disable react-hooks/exhaustive-deps */
/* eslint-disable @next/next/no-img-element */
import React, { useEffect, useState } from 'react';
import { useRouter } from 'next/router';
import { viewAuthorDetails } from '../../api/mergedData';

export default function ViewAuthors() {
  const [authorDetails, setAuthorDetails] = useState({});
  const router = useRouter();

  // TODO: grab firebaseKey from url
  const { firebaseKey } = router.query;

  // TODO: make call to API layer to get the data
  useEffect(() => {
    viewAuthorDetails(firebaseKey).then(setAuthorDetails);
  }, []);

  return (
    <div style={{ width: '18rem', margin: '10px' }}>
      <img src={authorDetails.image} alt={authorDetails.email} style={{ height: '400px' }} />
      <h2>{authorDetails.first_name} {authorDetails.last_name}</h2>
      <h3>{authorDetails.email}</h3>
    </div>
  );
}
