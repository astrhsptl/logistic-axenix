import {
  DefaultButton,
  DefaultInput,
  FormBaseLayout,
  useStoreHook,
} from '@/shared';
import { SubmitHandler, useForm } from 'react-hook-form';
import { BaseModal } from '.';

interface ModalFormData {
  email: string;
}

export const VovaModal = () => {
  const { cookiesStatement } = useStoreHook();

  const methods = useForm<ModalFormData>();
  const formOnSubmit: SubmitHandler<ModalFormData> = (data) => {
    console.log(data);
  };

  return (
    <BaseModal statement={cookiesStatement}>
      <FormBaseLayout methods={methods} onSub={formOnSubmit}>
        <DefaultInput
          name='email'
          placeholder='Email'
          registerOptions={{
            required: {
              value: true,
              message: 'Email обязателен',
            },
          }}
        />
        <DefaultButton type='submit'>Отправить</DefaultButton>
      </FormBaseLayout>

      <button onClick={cookiesStatement.switchState}>close</button>
    </BaseModal>
  );
};
