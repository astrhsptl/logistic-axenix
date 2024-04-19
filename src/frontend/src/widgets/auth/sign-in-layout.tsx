import { useSignIn } from '@/features';
import {
  AuthStyles,
  DefaultButton,
  DefaultInput,
  FormBaseLayout,
} from '@/shared';
import React, { useState } from 'react';
import { SubmitHandler, useForm } from 'react-hook-form';
import toast, { Toaster } from 'react-hot-toast';
import { useNavigate } from 'react-router-dom';

interface SignInLayoutProps {}
interface SignInData {
  username: string;
  password: string;
}

export const SignInLayout: React.FC<SignInLayoutProps> = () => {
  const methods = useForm();
  const navigate = useNavigate();

  const [isLoading, setIsLoading] = useState(false);
  const submit: SubmitHandler<SignInData> = async (credentials) => {
    setIsLoading(true);
    const tokens = await useSignIn(credentials).then((data) => {
      setIsLoading(false);
      return data;
    });

    if (!tokens) {
      return toast.error('Неверные данные');
    }

    toast.success('Удачно!');
    return setTimeout(() => {
      return navigate('/');
    }, 1500);
  };
  return (
    <article className={AuthStyles.authForm}>
      <h2>Вход</h2>
      <FormBaseLayout methods={methods} onSub={submit}>
        <DefaultInput
          name='username'
          placeholder='Nick name'
          registerOptions={{
            required: {
              value: true,
              message: 'Обязательное поле',
            },
          }}
        />
        <DefaultInput
          name='password'
          placeholder='Пароль'
          registerOptions={{
            required: {
              value: true,
              message: 'Обязательное поле',
            },
          }}
        />
        <DefaultButton isLoading={isLoading} type='submit'>
          Войти
        </DefaultButton>
      </FormBaseLayout>
      <Toaster />
    </article>
  );
};
