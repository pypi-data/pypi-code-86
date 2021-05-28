depends = ('ITKPyBase', 'ITKStatistics', 'ITKImageFilterBase', 'ITKCommon', )
templates = (
  ('CompositeTransform', 'itk::CompositeTransform', 'itkCompositeTransformD2', True, 'double,2'),
  ('CompositeTransform', 'itk::CompositeTransform', 'itkCompositeTransformD3', True, 'double,3'),
  ('CompositeTransform', 'itk::CompositeTransform', 'itkCompositeTransformD4', True, 'double,4'),
  ('TransformBaseTemplateEnums', 'itk::TransformBaseTemplateEnums', 'itkTransformBaseTemplateEnums', False),
  ('TransformBaseTemplate', 'itk::TransformBaseTemplate', 'itkTransformBaseTemplateD', False, 'double'),
  ('list', 'std::list', 'listitkTransformBaseTemplateD_Pointer', False, 'itk::TransformBaseTemplate< double  >'),
  ('TransformBaseTemplate', 'itk::TransformBaseTemplate', 'itkTransformBaseTemplateF', False, 'float'),
  ('list', 'std::list', 'listitkTransformBaseTemplateF_Pointer', False, 'itk::TransformBaseTemplate< float  >'),
  ('Transform', 'itk::Transform', 'itkTransformD22', True, 'double,2,2'),
  ('Transform', 'itk::Transform', 'itkTransformF22', True, 'float,2,2'),
  ('Transform', 'itk::Transform', 'itkTransformD23', True, 'double,2,3'),
  ('Transform', 'itk::Transform', 'itkTransformF23', True, 'float,2,3'),
  ('Transform', 'itk::Transform', 'itkTransformD24', True, 'double,2,4'),
  ('Transform', 'itk::Transform', 'itkTransformF24', True, 'float,2,4'),
  ('Transform', 'itk::Transform', 'itkTransformD32', True, 'double,3,2'),
  ('Transform', 'itk::Transform', 'itkTransformF32', True, 'float,3,2'),
  ('Transform', 'itk::Transform', 'itkTransformD33', True, 'double,3,3'),
  ('Transform', 'itk::Transform', 'itkTransformF33', True, 'float,3,3'),
  ('Transform', 'itk::Transform', 'itkTransformD34', True, 'double,3,4'),
  ('Transform', 'itk::Transform', 'itkTransformF34', True, 'float,3,4'),
  ('Transform', 'itk::Transform', 'itkTransformD42', True, 'double,4,2'),
  ('Transform', 'itk::Transform', 'itkTransformF42', True, 'float,4,2'),
  ('Transform', 'itk::Transform', 'itkTransformD43', True, 'double,4,3'),
  ('Transform', 'itk::Transform', 'itkTransformF43', True, 'float,4,3'),
  ('Transform', 'itk::Transform', 'itkTransformD44', True, 'double,4,4'),
  ('Transform', 'itk::Transform', 'itkTransformF44', True, 'float,4,4'),
  ('Transform', 'itk::Transform', 'itkTransformD2', True, 'double,2'),
  ('Transform', 'itk::Transform', 'itkTransformF2', True, 'float,2'),
  ('Transform', 'itk::Transform', 'itkTransformD3', True, 'double,3'),
  ('Transform', 'itk::Transform', 'itkTransformF3', True, 'float,3'),
  ('Transform', 'itk::Transform', 'itkTransformD4', True, 'double,4'),
  ('Transform', 'itk::Transform', 'itkTransformF4', True, 'float,4'),
  ('DataObjectDecorator', 'itk::DataObjectDecorator', 'itkDataObjectDecoratorTD22', False, 'itk::Transform< double,2,2 >'),
  ('DataObjectDecorator', 'itk::DataObjectDecorator', 'itkDataObjectDecoratorTF22', False, 'itk::Transform< float,2,2 >'),
  ('DataObjectDecorator', 'itk::DataObjectDecorator', 'itkDataObjectDecoratorTD23', False, 'itk::Transform< double,2,3 >'),
  ('DataObjectDecorator', 'itk::DataObjectDecorator', 'itkDataObjectDecoratorTF23', False, 'itk::Transform< float,2,3 >'),
  ('DataObjectDecorator', 'itk::DataObjectDecorator', 'itkDataObjectDecoratorTD24', False, 'itk::Transform< double,2,4 >'),
  ('DataObjectDecorator', 'itk::DataObjectDecorator', 'itkDataObjectDecoratorTF24', False, 'itk::Transform< float,2,4 >'),
  ('DataObjectDecorator', 'itk::DataObjectDecorator', 'itkDataObjectDecoratorTD32', False, 'itk::Transform< double,3,2 >'),
  ('DataObjectDecorator', 'itk::DataObjectDecorator', 'itkDataObjectDecoratorTF32', False, 'itk::Transform< float,3,2 >'),
  ('DataObjectDecorator', 'itk::DataObjectDecorator', 'itkDataObjectDecoratorTD33', False, 'itk::Transform< double,3,3 >'),
  ('DataObjectDecorator', 'itk::DataObjectDecorator', 'itkDataObjectDecoratorTF33', False, 'itk::Transform< float,3,3 >'),
  ('DataObjectDecorator', 'itk::DataObjectDecorator', 'itkDataObjectDecoratorTD34', False, 'itk::Transform< double,3,4 >'),
  ('DataObjectDecorator', 'itk::DataObjectDecorator', 'itkDataObjectDecoratorTF34', False, 'itk::Transform< float,3,4 >'),
  ('DataObjectDecorator', 'itk::DataObjectDecorator', 'itkDataObjectDecoratorTD42', False, 'itk::Transform< double,4,2 >'),
  ('DataObjectDecorator', 'itk::DataObjectDecorator', 'itkDataObjectDecoratorTF42', False, 'itk::Transform< float,4,2 >'),
  ('DataObjectDecorator', 'itk::DataObjectDecorator', 'itkDataObjectDecoratorTD43', False, 'itk::Transform< double,4,3 >'),
  ('DataObjectDecorator', 'itk::DataObjectDecorator', 'itkDataObjectDecoratorTF43', False, 'itk::Transform< float,4,3 >'),
  ('DataObjectDecorator', 'itk::DataObjectDecorator', 'itkDataObjectDecoratorTD44', False, 'itk::Transform< double,4,4 >'),
  ('DataObjectDecorator', 'itk::DataObjectDecorator', 'itkDataObjectDecoratorTF44', False, 'itk::Transform< float,4,4 >'),
  ('MatrixOffsetTransformBase', 'itk::MatrixOffsetTransformBase', 'itkMatrixOffsetTransformBaseD22', True, 'double,2,2'),
  ('MatrixOffsetTransformBase', 'itk::MatrixOffsetTransformBase', 'itkMatrixOffsetTransformBaseF22', True, 'float,2,2'),
  ('MatrixOffsetTransformBase', 'itk::MatrixOffsetTransformBase', 'itkMatrixOffsetTransformBaseD33', True, 'double,3,3'),
  ('MatrixOffsetTransformBase', 'itk::MatrixOffsetTransformBase', 'itkMatrixOffsetTransformBaseF33', True, 'float,3,3'),
  ('MatrixOffsetTransformBase', 'itk::MatrixOffsetTransformBase', 'itkMatrixOffsetTransformBaseD44', True, 'double,4,4'),
  ('MatrixOffsetTransformBase', 'itk::MatrixOffsetTransformBase', 'itkMatrixOffsetTransformBaseF44', True, 'float,4,4'),
  ('Euler2DTransform', 'itk::Euler2DTransform', 'itkEuler2DTransformD', True, 'double'),
  ('Euler3DTransform', 'itk::Euler3DTransform', 'itkEuler3DTransformD', True, 'double'),
  ('MultiTransform', 'itk::MultiTransform', 'itkMultiTransformD22', True, 'double,2,2'),
  ('MultiTransform', 'itk::MultiTransform', 'itkMultiTransformD33', True, 'double,3,3'),
  ('MultiTransform', 'itk::MultiTransform', 'itkMultiTransformD44', True, 'double,4,4'),
  ('VersorTransform', 'itk::VersorTransform', 'itkVersorTransformD', True, 'double'),
  ('VersorRigid3DTransform', 'itk::VersorRigid3DTransform', 'itkVersorRigid3DTransformD', True, 'double'),
  ('Similarity2DTransform', 'itk::Similarity2DTransform', 'itkSimilarity2DTransformD', True, 'double'),
  ('Similarity3DTransform', 'itk::Similarity3DTransform', 'itkSimilarity3DTransformD', True, 'double'),
  ('AffineTransform', 'itk::AffineTransform', 'itkAffineTransformD2', True, 'double,2'),
  ('AffineTransform', 'itk::AffineTransform', 'itkAffineTransformD3', True, 'double,3'),
  ('AffineTransform', 'itk::AffineTransform', 'itkAffineTransformD4', True, 'double,4'),
  ('ScalableAffineTransform', 'itk::ScalableAffineTransform', 'itkScalableAffineTransformD2', True, 'double,2'),
  ('ScalableAffineTransform', 'itk::ScalableAffineTransform', 'itkScalableAffineTransformD3', True, 'double,3'),
  ('ScalableAffineTransform', 'itk::ScalableAffineTransform', 'itkScalableAffineTransformD4', True, 'double,4'),
  ('ScaleTransform', 'itk::ScaleTransform', 'itkScaleTransformD2', True, 'double,2'),
  ('ScaleTransform', 'itk::ScaleTransform', 'itkScaleTransformD3', True, 'double,3'),
  ('ScaleTransform', 'itk::ScaleTransform', 'itkScaleTransformD4', True, 'double,4'),
  ('KernelTransform', 'itk::KernelTransform', 'itkKernelTransformD2', True, 'double,2'),
  ('KernelTransform', 'itk::KernelTransform', 'itkKernelTransformD3', True, 'double,3'),
  ('KernelTransform', 'itk::KernelTransform', 'itkKernelTransformD4', True, 'double,4'),
  ('AzimuthElevationToCartesianTransform', 'itk::AzimuthElevationToCartesianTransform', 'itkAzimuthElevationToCartesianTransformD2', True, 'double,2'),
  ('AzimuthElevationToCartesianTransform', 'itk::AzimuthElevationToCartesianTransform', 'itkAzimuthElevationToCartesianTransformD3', True, 'double,3'),
  ('AzimuthElevationToCartesianTransform', 'itk::AzimuthElevationToCartesianTransform', 'itkAzimuthElevationToCartesianTransformD4', True, 'double,4'),
  ('BSplineBaseTransform', 'itk::BSplineBaseTransform', 'itkBSplineBaseTransformD23', True, 'double,2,3'),
  ('BSplineBaseTransform', 'itk::BSplineBaseTransform', 'itkBSplineBaseTransformD33', True, 'double,3,3'),
  ('BSplineBaseTransform', 'itk::BSplineBaseTransform', 'itkBSplineBaseTransformD43', True, 'double,4,3'),
  ('BSplineTransform', 'itk::BSplineTransform', 'itkBSplineTransformD23', True, 'double,2,3'),
  ('BSplineTransform', 'itk::BSplineTransform', 'itkBSplineTransformD33', True, 'double,3,3'),
  ('BSplineTransform', 'itk::BSplineTransform', 'itkBSplineTransformD43', True, 'double,4,3'),
  ('BSplineTransformInitializer', 'itk::BSplineTransformInitializer', 'itkBSplineTransformInitializerBSTD23ISS2', True, 'itk::BSplineTransform< double, 2, 3 >, itk::Image< signed short,2 >'),
  ('BSplineTransformInitializer', 'itk::BSplineTransformInitializer', 'itkBSplineTransformInitializerBSTD23IUC2', True, 'itk::BSplineTransform< double, 2, 3 >, itk::Image< unsigned char,2 >'),
  ('BSplineTransformInitializer', 'itk::BSplineTransformInitializer', 'itkBSplineTransformInitializerBSTD23IUS2', True, 'itk::BSplineTransform< double, 2, 3 >, itk::Image< unsigned short,2 >'),
  ('BSplineTransformInitializer', 'itk::BSplineTransformInitializer', 'itkBSplineTransformInitializerBSTD23IF2', True, 'itk::BSplineTransform< double, 2, 3 >, itk::Image< float,2 >'),
  ('BSplineTransformInitializer', 'itk::BSplineTransformInitializer', 'itkBSplineTransformInitializerBSTD23ID2', True, 'itk::BSplineTransform< double, 2, 3 >, itk::Image< double,2 >'),
  ('BSplineTransformInitializer', 'itk::BSplineTransformInitializer', 'itkBSplineTransformInitializerBSTD33ISS3', True, 'itk::BSplineTransform< double, 3, 3 >, itk::Image< signed short,3 >'),
  ('BSplineTransformInitializer', 'itk::BSplineTransformInitializer', 'itkBSplineTransformInitializerBSTD33IUC3', True, 'itk::BSplineTransform< double, 3, 3 >, itk::Image< unsigned char,3 >'),
  ('BSplineTransformInitializer', 'itk::BSplineTransformInitializer', 'itkBSplineTransformInitializerBSTD33IUS3', True, 'itk::BSplineTransform< double, 3, 3 >, itk::Image< unsigned short,3 >'),
  ('BSplineTransformInitializer', 'itk::BSplineTransformInitializer', 'itkBSplineTransformInitializerBSTD33IF3', True, 'itk::BSplineTransform< double, 3, 3 >, itk::Image< float,3 >'),
  ('BSplineTransformInitializer', 'itk::BSplineTransformInitializer', 'itkBSplineTransformInitializerBSTD33ID3', True, 'itk::BSplineTransform< double, 3, 3 >, itk::Image< double,3 >'),
  ('BSplineTransformInitializer', 'itk::BSplineTransformInitializer', 'itkBSplineTransformInitializerBSTD43ISS4', True, 'itk::BSplineTransform< double, 4, 3 >, itk::Image< signed short,4 >'),
  ('BSplineTransformInitializer', 'itk::BSplineTransformInitializer', 'itkBSplineTransformInitializerBSTD43IUC4', True, 'itk::BSplineTransform< double, 4, 3 >, itk::Image< unsigned char,4 >'),
  ('BSplineTransformInitializer', 'itk::BSplineTransformInitializer', 'itkBSplineTransformInitializerBSTD43IUS4', True, 'itk::BSplineTransform< double, 4, 3 >, itk::Image< unsigned short,4 >'),
  ('BSplineTransformInitializer', 'itk::BSplineTransformInitializer', 'itkBSplineTransformInitializerBSTD43IF4', True, 'itk::BSplineTransform< double, 4, 3 >, itk::Image< float,4 >'),
  ('BSplineTransformInitializer', 'itk::BSplineTransformInitializer', 'itkBSplineTransformInitializerBSTD43ID4', True, 'itk::BSplineTransform< double, 4, 3 >, itk::Image< double,4 >'),
  ('CenteredAffineTransform', 'itk::CenteredAffineTransform', 'itkCenteredAffineTransformD2', True, 'double,2'),
  ('CenteredAffineTransform', 'itk::CenteredAffineTransform', 'itkCenteredAffineTransformD3', True, 'double,3'),
  ('CenteredAffineTransform', 'itk::CenteredAffineTransform', 'itkCenteredAffineTransformD4', True, 'double,4'),
  ('CenteredEuler3DTransform', 'itk::CenteredEuler3DTransform', 'itkCenteredEuler3DTransformD', True, 'double'),
  ('CenteredRigid2DTransform', 'itk::CenteredRigid2DTransform', 'itkCenteredRigid2DTransformD', True, 'double'),
  ('CenteredSimilarity2DTransform', 'itk::CenteredSimilarity2DTransform', 'itkCenteredSimilarity2DTransformD', True, 'double'),
  ('ComposeScaleSkewVersor3DTransform', 'itk::ComposeScaleSkewVersor3DTransform', 'itkComposeScaleSkewVersor3DTransformD', True, 'double'),
  ('ElasticBodyReciprocalSplineKernelTransform', 'itk::ElasticBodyReciprocalSplineKernelTransform', 'itkElasticBodyReciprocalSplineKernelTransformD2', True, 'double,2'),
  ('ElasticBodyReciprocalSplineKernelTransform', 'itk::ElasticBodyReciprocalSplineKernelTransform', 'itkElasticBodyReciprocalSplineKernelTransformD3', True, 'double,3'),
  ('ElasticBodyReciprocalSplineKernelTransform', 'itk::ElasticBodyReciprocalSplineKernelTransform', 'itkElasticBodyReciprocalSplineKernelTransformD4', True, 'double,4'),
  ('ElasticBodySplineKernelTransform', 'itk::ElasticBodySplineKernelTransform', 'itkElasticBodySplineKernelTransformD2', True, 'double,2'),
  ('ElasticBodySplineKernelTransform', 'itk::ElasticBodySplineKernelTransform', 'itkElasticBodySplineKernelTransformD3', True, 'double,3'),
  ('ElasticBodySplineKernelTransform', 'itk::ElasticBodySplineKernelTransform', 'itkElasticBodySplineKernelTransformD4', True, 'double,4'),
  ('FixedCenterOfRotationAffineTransform', 'itk::FixedCenterOfRotationAffineTransform', 'itkFixedCenterOfRotationAffineTransformD2', True, 'double,2'),
  ('FixedCenterOfRotationAffineTransform', 'itk::FixedCenterOfRotationAffineTransform', 'itkFixedCenterOfRotationAffineTransformD3', True, 'double,3'),
  ('FixedCenterOfRotationAffineTransform', 'itk::FixedCenterOfRotationAffineTransform', 'itkFixedCenterOfRotationAffineTransformD4', True, 'double,4'),
  ('IdentityTransform', 'itk::IdentityTransform', 'itkIdentityTransformD2', True, 'double,2'),
  ('IdentityTransform', 'itk::IdentityTransform', 'itkIdentityTransformD3', True, 'double,3'),
  ('IdentityTransform', 'itk::IdentityTransform', 'itkIdentityTransformD4', True, 'double,4'),
  ('QuaternionRigidTransform', 'itk::QuaternionRigidTransform', 'itkQuaternionRigidTransformD', True, 'double'),
  ('Rigid2DTransform', 'itk::Rigid2DTransform', 'itkRigid2DTransformD', True, 'double'),
  ('Rigid3DPerspectiveTransform', 'itk::Rigid3DPerspectiveTransform', 'itkRigid3DPerspectiveTransformD', True, 'double'),
  ('Rigid3DTransform', 'itk::Rigid3DTransform', 'itkRigid3DTransformD', True, 'double'),
  ('ScaleLogarithmicTransform', 'itk::ScaleLogarithmicTransform', 'itkScaleLogarithmicTransformD2', True, 'double,2'),
  ('ScaleLogarithmicTransform', 'itk::ScaleLogarithmicTransform', 'itkScaleLogarithmicTransformD3', True, 'double,3'),
  ('ScaleLogarithmicTransform', 'itk::ScaleLogarithmicTransform', 'itkScaleLogarithmicTransformD4', True, 'double,4'),
  ('ScaleSkewVersor3DTransform', 'itk::ScaleSkewVersor3DTransform', 'itkScaleSkewVersor3DTransformD', True, 'double'),
  ('ScaleVersor3DTransform', 'itk::ScaleVersor3DTransform', 'itkScaleVersor3DTransformD', True, 'double'),
  ('ThinPlateR2LogRSplineKernelTransform', 'itk::ThinPlateR2LogRSplineKernelTransform', 'itkThinPlateR2LogRSplineKernelTransformD2', True, 'double,2'),
  ('ThinPlateR2LogRSplineKernelTransform', 'itk::ThinPlateR2LogRSplineKernelTransform', 'itkThinPlateR2LogRSplineKernelTransformD3', True, 'double,3'),
  ('ThinPlateR2LogRSplineKernelTransform', 'itk::ThinPlateR2LogRSplineKernelTransform', 'itkThinPlateR2LogRSplineKernelTransformD4', True, 'double,4'),
  ('ThinPlateSplineKernelTransform', 'itk::ThinPlateSplineKernelTransform', 'itkThinPlateSplineKernelTransformD2', True, 'double,2'),
  ('ThinPlateSplineKernelTransform', 'itk::ThinPlateSplineKernelTransform', 'itkThinPlateSplineKernelTransformD3', True, 'double,3'),
  ('ThinPlateSplineKernelTransform', 'itk::ThinPlateSplineKernelTransform', 'itkThinPlateSplineKernelTransformD4', True, 'double,4'),
  ('TranslationTransform', 'itk::TranslationTransform', 'itkTranslationTransformD2', True, 'double,2'),
  ('TranslationTransform', 'itk::TranslationTransform', 'itkTranslationTransformD3', True, 'double,3'),
  ('TranslationTransform', 'itk::TranslationTransform', 'itkTranslationTransformD4', True, 'double,4'),
  ('VolumeSplineKernelTransform', 'itk::VolumeSplineKernelTransform', 'itkVolumeSplineKernelTransformD2', True, 'double,2'),
  ('VolumeSplineKernelTransform', 'itk::VolumeSplineKernelTransform', 'itkVolumeSplineKernelTransformD3', True, 'double,3'),
  ('VolumeSplineKernelTransform', 'itk::VolumeSplineKernelTransform', 'itkVolumeSplineKernelTransformD4', True, 'double,4'),
)
