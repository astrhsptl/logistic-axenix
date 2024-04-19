import { useSignUp } from '@/features';
import {
  AuthStyles,
  DefaultButton,
  DefaultInput,
  FormBaseLayout,
} from '@/shared';
import { FC, useState } from 'react';
import { SubmitHandler, useForm } from 'react-hook-form';
import toast, { Toaster } from 'react-hot-toast';
import { useNavigate } from 'react-router-dom';

interface SignUpData {
  username: string;
  email: string;
  password: string;
}

export const SignUpLayout: FC = () => {
  const methods = useForm();
  const navigate = useNavigate();
  const [isLoading, setIsLoading] = useState(false);

  const submit: SubmitHandler<SignUpData> = async (credentials) => {
    setIsLoading(true);
    const tokens = await useSignUp(credentials).then((data) => {
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
      <h2>Регистрация</h2>
      <FormBaseLayout methods={methods} onSub={submit}>
        <DefaultInput
          name='email'
          placeholder='Email'
          registerOptions={{
            required: {
              value: true,
              message: 'Обязательное поле',
            },
            pattern: {
              value: /^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/,
              message: 'Неверный формат email',
            },
          }}
        />
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
          Регистрация
        </DefaultButton>
      </FormBaseLayout>
      <Toaster />
    </article>
  );
};
