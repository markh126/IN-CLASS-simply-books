/* eslint-disable react-hooks/exhaustive-deps */
import React, { useEffect, useState } from 'react';
import { getFavoriteAuthor } from '../../api/authorData';
import { useAuth } from '../../utils/context/authContext';
import AuthorCard from '../../components/AuthorCard';

export default function FavoriteAuthor() {
  const { user } = useAuth();
  const [favoriteAuthor, setFavoriteAuthor] = useState([]);

  const getAllFavoriteAuthors = () => {
    getFavoriteAuthor(user.uid).then(setFavoriteAuthor);
  };

  useEffect(() => {
    getAllFavoriteAuthors();
  }, []);

  return (
    <div>{favoriteAuthor.map((author) => (
      <AuthorCard key={author.firebaseKey} authorObj={author} onUpdate={getAllFavoriteAuthors} />
    ))}
    </div>
  );
}
