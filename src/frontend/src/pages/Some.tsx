import { VovaModal } from '@/features/modal/vova-modal';
import { useStoreHook } from '@/shared';
import { Header } from '@/widgets';
import { observer } from 'mobx-react-lite';

export const PenisForm = observer(() => {
  const {
    cookiesStatement: { switchState },
  } = useStoreHook();

  return (
    <div>
      <Header />
      <button onClick={switchState}>sadfg</button>
      <VovaModal />
    </div>
  );
});
