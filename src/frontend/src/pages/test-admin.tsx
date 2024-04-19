import { BaseAdminLayout } from '@/features';
import React from 'react';

interface TestAdminProps {}

const links = [
  { name: 'some', link: 'asdf' },
  { name: 'Test admin', link: 'test-admin' },
];

export const TestAdmin: React.FC<TestAdminProps> = () => {
  return <BaseAdminLayout links={links}>asdfkljahsdf</BaseAdminLayout>;
};
